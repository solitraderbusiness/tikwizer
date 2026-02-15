import { create } from 'zustand';
import {
  type Node,
  type Edge,
  type OnNodesChange,
  type OnEdgesChange,
  type Connection,
  applyNodeChanges,
  applyEdgeChanges,
  addEdge,
} from '@xyflow/react';
import type { EventName, FlowNodeData, ClipboardPayload, ClipboardEdge } from '../types';
import { uid } from '../lib/uid';

// Use generic Node without type param to avoid Record<string, unknown> constraint issues
type FlowNode = Node<FlowNodeData>;

export interface EventGraphData {
  nodes: FlowNode[];
  edges: Edge[];
}

interface EditorState {
  eventGraphs: Record<EventName, EventGraphData>;
  activeEvent: EventName;
  selectedNodeId: string | null;
  nextIdByUser: number;
  clipboard: ClipboardPayload | null;

  nodes: () => FlowNode[];
  edges: () => Edge[];

  setActiveEvent: (event: EventName) => void;
  setSelectedNode: (id: string | null) => void;
  onNodesChange: OnNodesChange<FlowNode>;
  onEdgesChange: OnEdgesChange;
  onConnect: (connection: Connection) => void;
  addNode: (node: FlowNode) => void;
  removeNode: (id: string) => void;
  updateNodeData: (id: string, data: Partial<FlowNodeData>) => void;
  loadStrategy: (eventGraphs: Record<EventName, EventGraphData>) => void;

  getSelectedNodeIds: () => string[];
  duplicateNode: (nodeId: string) => void;
  duplicateNodes: (nodeIds: string[]) => void;
  detachNode: (nodeId: string) => void;
  removeEdge: (edgeId: string) => void;
  removeSelectedNodes: () => void;
  copyNodes: (nodeIds: string[]) => void;
  cutNodes: (nodeIds: string[]) => void;
  pasteNodes: (position: { x: number; y: number }) => void;
  createGroup: (nodeIds: string[]) => void;
}

const emptyEventGraphs = (): Record<EventName, EventGraphData> => ({
  on_tick: { nodes: [], edges: [] },
  on_init: { nodes: [], edges: [] },
  on_timer: { nodes: [], edges: [] },
  on_trade: { nodes: [], edges: [] },
  on_chart: { nodes: [], edges: [] },
  on_deinit: { nodes: [], edges: [] },
});

export const useEditorStore = create<EditorState>((set, get) => ({
  eventGraphs: emptyEventGraphs(),
  activeEvent: 'on_tick',
  selectedNodeId: null,
  nextIdByUser: 1,
  clipboard: null,

  nodes: () => get().eventGraphs[get().activeEvent].nodes,
  edges: () => get().eventGraphs[get().activeEvent].edges,

  setActiveEvent: (event) => set({ activeEvent: event, selectedNodeId: null }),
  setSelectedNode: (id) => set({ selectedNodeId: id }),

  onNodesChange: (changes) => {
    const { activeEvent, eventGraphs } = get();
    const currentGraph = eventGraphs[activeEvent];
    set({
      eventGraphs: {
        ...eventGraphs,
        [activeEvent]: {
          ...currentGraph,
          nodes: applyNodeChanges(changes, currentGraph.nodes),
        },
      },
    });
  },

  onEdgesChange: (changes) => {
    const { activeEvent, eventGraphs } = get();
    const currentGraph = eventGraphs[activeEvent];
    set({
      eventGraphs: {
        ...eventGraphs,
        [activeEvent]: {
          ...currentGraph,
          edges: applyEdgeChanges(changes, currentGraph.edges),
        },
      },
    });
  },

  onConnect: (connection) => {
    const { activeEvent, eventGraphs } = get();
    const currentGraph = eventGraphs[activeEvent];
    const newEdge: Edge = {
      ...connection,
      type: 'conditionalEdge',
      id: `edge-${Date.now()}`,
      source: connection.source,
      target: connection.target,
    };
    set({
      eventGraphs: {
        ...eventGraphs,
        [activeEvent]: {
          ...currentGraph,
          edges: addEdge(newEdge, currentGraph.edges),
        },
      },
    });
  },

  addNode: (node) => {
    const { activeEvent, eventGraphs, nextIdByUser } = get();
    const currentGraph = eventGraphs[activeEvent];
    const nodeWithId = {
      ...node,
      data: { ...node.data, id_by_user: nextIdByUser },
    };
    set({
      eventGraphs: {
        ...eventGraphs,
        [activeEvent]: {
          ...currentGraph,
          nodes: [...currentGraph.nodes, nodeWithId],
        },
      },
      nextIdByUser: nextIdByUser + 1,
    });
  },

  removeNode: (id) => {
    const { activeEvent, eventGraphs } = get();
    const currentGraph = eventGraphs[activeEvent];
    set({
      eventGraphs: {
        ...eventGraphs,
        [activeEvent]: {
          nodes: currentGraph.nodes.filter((n) => n.id !== id),
          edges: currentGraph.edges.filter((e) => e.source !== id && e.target !== id),
        },
      },
      selectedNodeId: null,
    });
  },

  updateNodeData: (id, data) => {
    const { activeEvent, eventGraphs } = get();
    const currentGraph = eventGraphs[activeEvent];
    set({
      eventGraphs: {
        ...eventGraphs,
        [activeEvent]: {
          ...currentGraph,
          nodes: currentGraph.nodes.map((n) =>
            n.id === id ? { ...n, data: { ...n.data, ...data } } : n
          ),
        },
      },
    });
  },

  loadStrategy: (newEventGraphs) => {
    set({ eventGraphs: newEventGraphs, selectedNodeId: null });
  },

  getSelectedNodeIds: () => {
    const { activeEvent, eventGraphs } = get();
    return eventGraphs[activeEvent].nodes
      .filter((n) => n.selected)
      .map((n) => n.id);
  },

  duplicateNode: (nodeId) => {
    get().duplicateNodes([nodeId]);
  },

  duplicateNodes: (nodeIds) => {
    const { activeEvent, eventGraphs } = get();
    let { nextIdByUser } = get();
    const currentGraph = eventGraphs[activeEvent];
    const idMap = new Map<string, string>();

    const newNodes: FlowNode[] = [];
    for (const id of nodeIds) {
      const original = currentGraph.nodes.find((n) => n.id === id);
      if (!original) continue;
      const newId = uid();
      idMap.set(id, newId);
      newNodes.push({
        ...original,
        id: newId,
        position: { x: original.position.x + 40, y: original.position.y + 40 },
        selected: false,
        data: { ...original.data, id_by_user: nextIdByUser },
      });
      nextIdByUser++;
    }

    // Remap internal edges between duplicated nodes
    const newEdges: Edge[] = [];
    for (const edge of currentGraph.edges) {
      if (idMap.has(edge.source) && idMap.has(edge.target)) {
        newEdges.push({
          ...edge,
          id: `edge-${uid()}`,
          source: idMap.get(edge.source)!,
          target: idMap.get(edge.target)!,
        });
      }
    }

    set({
      eventGraphs: {
        ...eventGraphs,
        [activeEvent]: {
          nodes: [...currentGraph.nodes, ...newNodes],
          edges: [...currentGraph.edges, ...newEdges],
        },
      },
      nextIdByUser,
    });
  },

  detachNode: (nodeId) => {
    const { activeEvent, eventGraphs } = get();
    const currentGraph = eventGraphs[activeEvent];
    set({
      eventGraphs: {
        ...eventGraphs,
        [activeEvent]: {
          ...currentGraph,
          edges: currentGraph.edges.filter(
            (e) => e.source !== nodeId && e.target !== nodeId
          ),
        },
      },
    });
  },

  removeEdge: (edgeId) => {
    const { activeEvent, eventGraphs } = get();
    const currentGraph = eventGraphs[activeEvent];
    set({
      eventGraphs: {
        ...eventGraphs,
        [activeEvent]: {
          ...currentGraph,
          edges: currentGraph.edges.filter((e) => e.id !== edgeId),
        },
      },
    });
  },

  removeSelectedNodes: () => {
    const { activeEvent, eventGraphs } = get();
    const currentGraph = eventGraphs[activeEvent];
    const selectedIds = new Set(
      currentGraph.nodes.filter((n) => n.selected).map((n) => n.id)
    );
    if (selectedIds.size === 0) return;
    set({
      eventGraphs: {
        ...eventGraphs,
        [activeEvent]: {
          nodes: currentGraph.nodes.filter((n) => !selectedIds.has(n.id)),
          edges: currentGraph.edges.filter(
            (e) => !selectedIds.has(e.source) && !selectedIds.has(e.target)
          ),
        },
      },
      selectedNodeId: null,
    });
  },

  copyNodes: (nodeIds) => {
    const { activeEvent, eventGraphs } = get();
    const currentGraph = eventGraphs[activeEvent];
    const nodeSet = new Set(nodeIds);
    const matchedNodes = currentGraph.nodes.filter((n) => nodeSet.has(n.id));
    if (matchedNodes.length === 0) return;

    // Calculate centroid for relative positions
    const cx = matchedNodes.reduce((s, n) => s + n.position.x, 0) / matchedNodes.length;
    const cy = matchedNodes.reduce((s, n) => s + n.position.y, 0) / matchedNodes.length;

    const clipboardNodes = matchedNodes.map((n) => ({
      type: n.type || 'conditionNode',
      data: { ...n.data } as FlowNodeData,
      relativePosition: { x: n.position.x - cx, y: n.position.y - cy },
    }));

    // Internal edges only
    const clipboardEdges: ClipboardEdge[] = currentGraph.edges
      .filter((e) => nodeSet.has(e.source) && nodeSet.has(e.target))
      .map((e, i) => ({
        id: `clip-edge-${i}`,
        source: String(nodeIds.indexOf(e.source)),
        target: String(nodeIds.indexOf(e.target)),
        sourceHandle: e.sourceHandle,
        targetHandle: e.targetHandle,
        type: e.type,
      }));

    set({ clipboard: { nodes: clipboardNodes, edges: clipboardEdges } });
  },

  cutNodes: (nodeIds) => {
    get().copyNodes(nodeIds);
    // Now remove the nodes
    const { activeEvent, eventGraphs } = get();
    const currentGraph = eventGraphs[activeEvent];
    const nodeSet = new Set(nodeIds);
    set({
      eventGraphs: {
        ...eventGraphs,
        [activeEvent]: {
          nodes: currentGraph.nodes.filter((n) => !nodeSet.has(n.id)),
          edges: currentGraph.edges.filter(
            (e) => !nodeSet.has(e.source) && !nodeSet.has(e.target)
          ),
        },
      },
      selectedNodeId: null,
    });
  },

  pasteNodes: (position) => {
    const { clipboard, activeEvent, eventGraphs } = get();
    if (!clipboard || clipboard.nodes.length === 0) return;
    let { nextIdByUser } = get();
    const currentGraph = eventGraphs[activeEvent];

    const newIds: string[] = [];
    const newNodes: FlowNode[] = clipboard.nodes.map((cn) => {
      const newId = uid();
      newIds.push(newId);
      return {
        id: newId,
        type: cn.type,
        position: {
          x: position.x + cn.relativePosition.x,
          y: position.y + cn.relativePosition.y,
        },
        data: { ...cn.data, id_by_user: nextIdByUser++ },
        selected: false,
      };
    });

    const newEdges: Edge[] = clipboard.edges.map((ce) => ({
      ...ce,
      id: `edge-${uid()}`,
      source: newIds[Number(ce.source)] || ce.source,
      target: newIds[Number(ce.target)] || ce.target,
    }));

    set({
      eventGraphs: {
        ...eventGraphs,
        [activeEvent]: {
          nodes: [...currentGraph.nodes, ...newNodes],
          edges: [...currentGraph.edges, ...newEdges],
        },
      },
      nextIdByUser,
    });
  },

  createGroup: (nodeIds) => {
    const { activeEvent, eventGraphs, nextIdByUser } = get();
    const currentGraph = eventGraphs[activeEvent];
    const targetNodes = currentGraph.nodes.filter((n) => nodeIds.includes(n.id));
    if (targetNodes.length < 2) return;

    // Calculate bounding box
    const padding = 40;
    const minX = Math.min(...targetNodes.map((n) => n.position.x)) - padding;
    const minY = Math.min(...targetNodes.map((n) => n.position.y)) - padding;
    const maxX = Math.max(...targetNodes.map((n) => n.position.x + 200)) + padding;
    const maxY = Math.max(...targetNodes.map((n) => n.position.y + 100)) + padding;

    const groupId = uid();
    const groupNode: FlowNode = {
      id: groupId,
      type: 'groupNode',
      position: { x: minX, y: minY },
      data: {
        blockName: 'Group',
        block_name_mql: '',
        category: 'group',
        params: {},
        enabled: true,
        id_by_user: nextIdByUser,
      },
      style: { width: maxX - minX, height: maxY - minY },
    };

    // Adjust child positions relative to group and set parentId
    const updatedNodes = currentGraph.nodes.map((n) => {
      if (nodeIds.includes(n.id)) {
        return {
          ...n,
          parentId: groupId,
          position: { x: n.position.x - minX, y: n.position.y - minY },
        };
      }
      return n;
    });

    set({
      eventGraphs: {
        ...eventGraphs,
        [activeEvent]: {
          ...currentGraph,
          nodes: [groupNode, ...updatedNodes],
        },
      },
      nextIdByUser: nextIdByUser + 1,
    });
  },
}));
