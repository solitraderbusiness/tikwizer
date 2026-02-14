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
import type { EventName, FlowNodeData } from '../types';

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
}));
