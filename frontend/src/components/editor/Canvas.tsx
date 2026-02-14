import { useCallback, useRef, type DragEvent } from 'react';
import {
  ReactFlow,
  Background,
  Controls,
} from '@xyflow/react';
import '@xyflow/react/dist/style.css';

import { useEditorStore } from '../../stores/editorStore';
import { ConditionNode } from './nodes/ConditionNode';
import { ActionNode } from './nodes/ActionNode';
import { FilterNode } from './nodes/FilterNode';
import { LoopNode } from './nodes/LoopNode';
import { ControlNode } from './nodes/ControlNode';
import { ConditionalEdge } from './edges/ConditionalEdge';

const nodeTypes = {
  conditionNode: ConditionNode,
  actionNode: ActionNode,
  filterNode: FilterNode,
  loopNode: LoopNode,
  controlNode: ControlNode,
};

const edgeTypes = {
  conditionalEdge: ConditionalEdge,
};

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

  const currentGraph = eventGraphs[activeEvent];

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
        id: crypto.randomUUID(),
        type: blockData.nodeType,
        position,
        data: {
          blockName: blockData.blockName,
          block_name_mql: blockData.block_name_mql,
          category: blockData.category,
          params: {},
          enabled: true,
          id_by_user: 0, // Will be set by addNode
        },
      };

      addNode(newNode);
    },
    [addNode],
  );

  return (
    <div ref={reactFlowWrapper} className="w-full h-full">
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
        onPaneClick={() => setSelectedNode(null)}
        fitView
        defaultEdgeOptions={{ type: 'conditionalEdge' }}
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
    </div>
  );
}
