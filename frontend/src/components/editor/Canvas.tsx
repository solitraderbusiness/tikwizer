import { useCallback, useEffect, useRef, useState, type DragEvent } from 'react';
import {
  ReactFlow,
  Background,
  Controls,
  type NodeMouseHandler,
  type EdgeMouseHandler,
} from '@xyflow/react';
import '@xyflow/react/dist/style.css';

import { useEditorStore } from '../../stores/editorStore';
import { useStrategyStore } from '../../stores/strategyStore';
import { uid } from '../../lib/uid';
import { ConditionNode } from './nodes/ConditionNode';
import { ActionNode } from './nodes/ActionNode';
import { FilterNode } from './nodes/FilterNode';
import { LoopNode } from './nodes/LoopNode';
import { ControlNode } from './nodes/ControlNode';
import { GroupNode } from './nodes/GroupNode';
import { ConditionalEdge } from './edges/ConditionalEdge';
import { NodeContextMenu } from './context-menu/NodeContextMenu';
import { EdgeContextMenu } from './context-menu/EdgeContextMenu';
import { CanvasContextMenu } from './context-menu/CanvasContextMenu';
import { InlineRenameInput } from './context-menu/InlineRenameInput';
import { NodeInfoPanel } from './context-menu/NodeInfoPanel';

const nodeTypes = {
  conditionNode: ConditionNode,
  actionNode: ActionNode,
  filterNode: FilterNode,
  loopNode: LoopNode,
  controlNode: ControlNode,
  groupNode: GroupNode,
};

const edgeTypes = {
  conditionalEdge: ConditionalEdge,
};

interface MenuState {
  id: string;
  x: number;
  y: number;
}

interface PaneMenuState {
  x: number;
  y: number;
  flowPosition: { x: number; y: number };
}

interface RenameState {
  nodeId: string;
  x: number;
  y: number;
}

interface InfoState {
  nodeId: string;
  x: number;
  y: number;
}

export function Canvas() {
  const reactFlowWrapper = useRef<HTMLDivElement>(null);
  const reactFlowInstance = useRef<any>(null);

  const eventGraphs = useEditorStore((s) => s.eventGraphs);
  const activeEvent = useEditorStore((s) => s.activeEvent);
  const onNodesChange = useEditorStore((s) => s.onNodesChange);
  const onEdgesChange = useEditorStore((s) => s.onEdgesChange);
  const onConnect = useEditorStore((s) => s.onConnect);
  const addNode = useEditorStore((s) => s.addNode);
  const setSelectedNode = useEditorStore((s) => s.setSelectedNode);
  const selectVarConst = useStrategyStore((s) => s.selectVarConst);

  const currentGraph = eventGraphs[activeEvent];

  // Context menu state
  const [nodeMenu, setNodeMenu] = useState<MenuState | null>(null);
  const [edgeMenu, setEdgeMenu] = useState<MenuState | null>(null);
  const [paneMenu, setPaneMenu] = useState<PaneMenuState | null>(null);
  const [renameState, setRenameState] = useState<RenameState | null>(null);
  const [infoNode, setInfoNode] = useState<InfoState | null>(null);

  const closeAllMenus = useCallback(() => {
    setNodeMenu(null);
    setEdgeMenu(null);
    setPaneMenu(null);
  }, []);

  const onNodeContextMenu: NodeMouseHandler = useCallback(
    (event, node) => {
      event.preventDefault();
      closeAllMenus();
      setNodeMenu({ id: node.id, x: event.clientX, y: event.clientY });
    },
    [closeAllMenus],
  );

  const onEdgeContextMenu: EdgeMouseHandler = useCallback(
    (event, edge) => {
      event.preventDefault();
      closeAllMenus();
      setEdgeMenu({ id: edge.id, x: event.clientX, y: event.clientY });
    },
    [closeAllMenus],
  );

  const onPaneContextMenu = useCallback(
    (event: React.MouseEvent | MouseEvent) => {
      event.preventDefault();
      closeAllMenus();
      const flowPos = reactFlowInstance.current?.screenToFlowPosition({
        x: event.clientX,
        y: event.clientY,
      }) ?? { x: 0, y: 0 };
      setPaneMenu({
        x: event.clientX,
        y: event.clientY,
        flowPosition: flowPos,
      });
    },
    [closeAllMenus],
  );

  const handleRename = useCallback((nodeId: string) => {
    // Position rename input near the node menu position
    setRenameState({ nodeId, x: nodeMenu?.x ?? 200, y: nodeMenu?.y ?? 200 });
  }, [nodeMenu]);

  const handleShowInfo = useCallback((nodeId: string) => {
    setInfoNode({ nodeId, x: nodeMenu?.x ?? 200, y: nodeMenu?.y ?? 200 });
  }, [nodeMenu]);

  // Keyboard shortcuts
  useEffect(() => {
    const wrapper = reactFlowWrapper.current;
    if (!wrapper) return;

    const handleKeyDown = (e: KeyboardEvent) => {
      const target = e.target as HTMLElement;
      if (
        target.tagName === 'INPUT' ||
        target.tagName === 'TEXTAREA' ||
        target.isContentEditable
      ) {
        return;
      }

      const store = useEditorStore.getState();

      if (e.key === 'Delete' || e.key === 'Backspace') {
        e.preventDefault();
        store.removeSelectedNodes();
      } else if (e.key === 'Escape') {
        closeAllMenus();
        setRenameState(null);
        setInfoNode(null);
      } else if (e.ctrlKey || e.metaKey) {
        const selectedIds = store.getSelectedNodeIds();
        if (e.key === 'c') {
          e.preventDefault();
          if (selectedIds.length > 0) store.copyNodes(selectedIds);
        } else if (e.key === 'x') {
          e.preventDefault();
          if (selectedIds.length > 0) store.cutNodes(selectedIds);
        } else if (e.key === 'v') {
          e.preventDefault();
          // Paste at viewport center
          const viewport = reactFlowInstance.current?.getViewport();
          const wrapper = reactFlowWrapper.current;
          if (viewport && wrapper) {
            const rect = wrapper.getBoundingClientRect();
            const center = reactFlowInstance.current.screenToFlowPosition({
              x: rect.width / 2,
              y: rect.height / 2,
            });
            store.pasteNodes(center);
          }
        } else if (e.key === 'd') {
          e.preventDefault();
          if (selectedIds.length > 0) store.duplicateNodes(selectedIds);
        }
      }
    };

    wrapper.addEventListener('keydown', handleKeyDown);
    return () => wrapper.removeEventListener('keydown', handleKeyDown);
  }, [closeAllMenus]);

  const onDragOver = useCallback((event: DragEvent) => {
    event.preventDefault();
    event.dataTransfer.dropEffect = 'move';
  }, []);

  const onDrop = useCallback(
    (event: DragEvent) => {
      event.preventDefault();
      const blockDataStr = event.dataTransfer.getData('application/tikwizer-block');
      if (!blockDataStr) return;

      const blockData = JSON.parse(blockDataStr);
      const bounds = reactFlowWrapper.current?.getBoundingClientRect();
      if (!bounds || !reactFlowInstance.current) return;

      const position = reactFlowInstance.current.screenToFlowPosition({
        x: event.clientX - bounds.left,
        y: event.clientY - bounds.top,
      });

      const newNode = {
        id: uid(),
        type: blockData.nodeType,
        position,
        data: {
          blockName: blockData.blockName,
          block_name_mql: blockData.block_name_mql,
          category: blockData.category,
          params: blockData.default_params || {},
          enabled: true,
          id_by_user: 0, // Will be set by addNode
        },
      };

      addNode(newNode);
    },
    [addNode],
  );

  return (
    <div ref={reactFlowWrapper} className="w-full h-full" tabIndex={0} style={{ outline: 'none' }}>
      <ReactFlow
        nodes={currentGraph.nodes}
        edges={currentGraph.edges}
        onNodesChange={onNodesChange}
        onEdgesChange={onEdgesChange}
        onConnect={onConnect}
        nodeTypes={nodeTypes}
        edgeTypes={edgeTypes}
        onInit={(instance) => { reactFlowInstance.current = instance; }}
        onDragOver={onDragOver}
        onDrop={onDrop}
        onPaneClick={() => {
          setSelectedNode(null);
          selectVarConst(null);
          closeAllMenus();
        }}
        onNodeClick={() => { selectVarConst(null); }}
        onNodeContextMenu={onNodeContextMenu}
        onEdgeContextMenu={onEdgeContextMenu}
        onPaneContextMenu={onPaneContextMenu}
        onMoveStart={closeAllMenus}
        fitView
        defaultEdgeOptions={{ type: 'conditionalEdge', interactionWidth: 20 }}
        style={{ backgroundColor: 'var(--color-bg)' }}
      >
        <Background color="var(--color-border)" gap={20} />
        <Controls
          style={{
            backgroundColor: 'var(--color-surface)',
            borderColor: 'var(--color-border)',
          }}
        />
      </ReactFlow>

      {nodeMenu && (
        <NodeContextMenu
          nodeId={nodeMenu.id}
          x={nodeMenu.x}
          y={nodeMenu.y}
          onClose={() => setNodeMenu(null)}
          onRename={handleRename}
          onShowInfo={handleShowInfo}
        />
      )}

      {edgeMenu && (
        <EdgeContextMenu
          edgeId={edgeMenu.id}
          x={edgeMenu.x}
          y={edgeMenu.y}
          onClose={() => setEdgeMenu(null)}
        />
      )}

      {paneMenu && (
        <CanvasContextMenu
          x={paneMenu.x}
          y={paneMenu.y}
          flowPosition={paneMenu.flowPosition}
          onClose={() => setPaneMenu(null)}
        />
      )}

      {renameState && (
        <InlineRenameInput
          nodeId={renameState.nodeId}
          x={renameState.x}
          y={renameState.y}
          onClose={() => setRenameState(null)}
        />
      )}

      {infoNode && (
        <NodeInfoPanel
          nodeId={infoNode.nodeId}
          x={infoNode.x}
          y={infoNode.y}
          onClose={() => setInfoNode(null)}
        />
      )}
    </div>
  );
}
