import { describe, it, expect, beforeEach } from 'vitest';
import { useEditorStore } from './editorStore';

describe('editorStore', () => {
  beforeEach(() => {
    useEditorStore.setState({
      eventGraphs: {
        on_tick: { nodes: [], edges: [] },
        on_init: { nodes: [], edges: [] },
        on_timer: { nodes: [], edges: [] },
        on_trade: { nodes: [], edges: [] },
        on_chart: { nodes: [], edges: [] },
        on_deinit: { nodes: [], edges: [] },
      },
      activeEvent: 'on_tick',
      selectedNodeId: null,
      nextIdByUser: 1,
    });
  });

  it('initializes with on_tick as active event', () => {
    expect(useEditorStore.getState().activeEvent).toBe('on_tick');
  });

  it('initializes with empty event graphs', () => {
    const state = useEditorStore.getState();
    const eventNames = ['on_tick', 'on_init', 'on_timer', 'on_trade', 'on_chart', 'on_deinit'] as const;
    for (const name of eventNames) {
      expect(state.eventGraphs[name].nodes).toEqual([]);
      expect(state.eventGraphs[name].edges).toEqual([]);
    }
  });

  it('initializes with nextIdByUser at 1', () => {
    expect(useEditorStore.getState().nextIdByUser).toBe(1);
  });

  it('initializes with no selected node', () => {
    expect(useEditorStore.getState().selectedNodeId).toBeNull();
  });

  it('switches active event', () => {
    useEditorStore.getState().setActiveEvent('on_init');
    expect(useEditorStore.getState().activeEvent).toBe('on_init');
  });

  it('clears selected node when switching events', () => {
    useEditorStore.setState({ selectedNodeId: 'some-node' });
    useEditorStore.getState().setActiveEvent('on_timer');
    expect(useEditorStore.getState().selectedNodeId).toBeNull();
  });

  it('adds a node and increments nextIdByUser', () => {
    const node = {
      id: 'new-node',
      type: 'actionNode',
      position: { x: 0, y: 0 },
      data: {
        blockName: 'Buy Now',
        block_name_mql: 'buy_now',
        category: 'buy_sell',
        params: {},
        enabled: true,
        id_by_user: 0,
      },
    };
    useEditorStore.getState().addNode(node);
    const state = useEditorStore.getState();
    expect(state.eventGraphs.on_tick.nodes).toHaveLength(1);
    expect(state.eventGraphs.on_tick.nodes[0].data.id_by_user).toBe(1);
    expect(state.nextIdByUser).toBe(2);
  });

  it('assigns sequential id_by_user values for multiple adds', () => {
    const makeNode = (id: string) => ({
      id,
      type: 'actionNode',
      position: { x: 0, y: 0 },
      data: { blockName: 'N', block_name_mql: 'n', category: 'c', params: {}, enabled: true, id_by_user: 0 },
    });

    useEditorStore.getState().addNode(makeNode('n1'));
    useEditorStore.getState().addNode(makeNode('n2'));
    useEditorStore.getState().addNode(makeNode('n3'));

    const state = useEditorStore.getState();
    expect(state.eventGraphs.on_tick.nodes[0].data.id_by_user).toBe(1);
    expect(state.eventGraphs.on_tick.nodes[1].data.id_by_user).toBe(2);
    expect(state.eventGraphs.on_tick.nodes[2].data.id_by_user).toBe(3);
    expect(state.nextIdByUser).toBe(4);
  });

  it('removes a node and its connected edges', () => {
    useEditorStore.setState({
      eventGraphs: {
        ...useEditorStore.getState().eventGraphs,
        on_tick: {
          nodes: [
            { id: 'n1', type: 'actionNode', position: { x: 0, y: 0 }, data: { blockName: 'A', block_name_mql: 'a', category: 'c', params: {}, enabled: true, id_by_user: 1 } },
            { id: 'n2', type: 'actionNode', position: { x: 0, y: 0 }, data: { blockName: 'B', block_name_mql: 'b', category: 'c', params: {}, enabled: true, id_by_user: 2 } },
          ],
          edges: [
            { id: 'e1', source: 'n1', target: 'n2', type: 'conditionalEdge' },
          ],
        },
      },
    });

    useEditorStore.getState().removeNode('n1');
    const state = useEditorStore.getState();
    expect(state.eventGraphs.on_tick.nodes).toHaveLength(1);
    expect(state.eventGraphs.on_tick.nodes[0].id).toBe('n2');
    expect(state.eventGraphs.on_tick.edges).toHaveLength(0);
  });

  it('removes edges where node is the target', () => {
    useEditorStore.setState({
      eventGraphs: {
        ...useEditorStore.getState().eventGraphs,
        on_tick: {
          nodes: [
            { id: 'n1', type: 'actionNode', position: { x: 0, y: 0 }, data: { blockName: 'A', block_name_mql: 'a', category: 'c', params: {}, enabled: true, id_by_user: 1 } },
            { id: 'n2', type: 'actionNode', position: { x: 0, y: 0 }, data: { blockName: 'B', block_name_mql: 'b', category: 'c', params: {}, enabled: true, id_by_user: 2 } },
          ],
          edges: [
            { id: 'e1', source: 'n1', target: 'n2', type: 'conditionalEdge' },
          ],
        },
      },
    });

    useEditorStore.getState().removeNode('n2');
    const state = useEditorStore.getState();
    expect(state.eventGraphs.on_tick.nodes).toHaveLength(1);
    expect(state.eventGraphs.on_tick.nodes[0].id).toBe('n1');
    expect(state.eventGraphs.on_tick.edges).toHaveLength(0);
  });

  it('clears selectedNodeId when removing a node', () => {
    useEditorStore.setState({
      selectedNodeId: 'n1',
      eventGraphs: {
        ...useEditorStore.getState().eventGraphs,
        on_tick: {
          nodes: [
            { id: 'n1', type: 'actionNode', position: { x: 0, y: 0 }, data: { blockName: 'A', block_name_mql: 'a', category: 'c', params: {}, enabled: true, id_by_user: 1 } },
          ],
          edges: [],
        },
      },
    });

    useEditorStore.getState().removeNode('n1');
    expect(useEditorStore.getState().selectedNodeId).toBeNull();
  });

  it('preserves unrelated edges when removing a node', () => {
    useEditorStore.setState({
      eventGraphs: {
        ...useEditorStore.getState().eventGraphs,
        on_tick: {
          nodes: [
            { id: 'n1', type: 'actionNode', position: { x: 0, y: 0 }, data: { blockName: 'A', block_name_mql: 'a', category: 'c', params: {}, enabled: true, id_by_user: 1 } },
            { id: 'n2', type: 'actionNode', position: { x: 50, y: 0 }, data: { blockName: 'B', block_name_mql: 'b', category: 'c', params: {}, enabled: true, id_by_user: 2 } },
            { id: 'n3', type: 'actionNode', position: { x: 100, y: 0 }, data: { blockName: 'C', block_name_mql: 'c', category: 'c', params: {}, enabled: true, id_by_user: 3 } },
          ],
          edges: [
            { id: 'e1', source: 'n1', target: 'n2', type: 'conditionalEdge' },
            { id: 'e2', source: 'n2', target: 'n3', type: 'conditionalEdge' },
          ],
        },
      },
    });

    useEditorStore.getState().removeNode('n1');
    const state = useEditorStore.getState();
    expect(state.eventGraphs.on_tick.edges).toHaveLength(1);
    expect(state.eventGraphs.on_tick.edges[0].id).toBe('e2');
  });

  it('updates node data partially', () => {
    useEditorStore.setState({
      eventGraphs: {
        ...useEditorStore.getState().eventGraphs,
        on_tick: {
          nodes: [
            { id: 'n1', type: 'actionNode', position: { x: 0, y: 0 }, data: { blockName: 'Buy', block_name_mql: 'buy_now', category: 'buy_sell', params: { lot: '0.01' }, enabled: true, id_by_user: 1 } },
          ],
          edges: [],
        },
      },
    });

    useEditorStore.getState().updateNodeData('n1', { enabled: false });
    const node = useEditorStore.getState().eventGraphs.on_tick.nodes[0];
    expect(node.data.enabled).toBe(false);
    expect(node.data.blockName).toBe('Buy'); // Unchanged
    expect(node.data.params.lot).toBe('0.01'); // Unchanged
  });

  it('updates node params via updateNodeData', () => {
    useEditorStore.setState({
      eventGraphs: {
        ...useEditorStore.getState().eventGraphs,
        on_tick: {
          nodes: [
            { id: 'n1', type: 'actionNode', position: { x: 0, y: 0 }, data: { blockName: 'Buy', block_name_mql: 'buy_now', category: 'buy_sell', params: { lot: '0.01' }, enabled: true, id_by_user: 1 } },
          ],
          edges: [],
        },
      },
    });

    useEditorStore.getState().updateNodeData('n1', { params: { lot: '0.10', sl: '50' } });
    const node = useEditorStore.getState().eventGraphs.on_tick.nodes[0];
    expect(node.data.params.lot).toBe('0.10');
    expect(node.data.params.sl).toBe('50');
  });

  it('does not modify other nodes when updating one', () => {
    useEditorStore.setState({
      eventGraphs: {
        ...useEditorStore.getState().eventGraphs,
        on_tick: {
          nodes: [
            { id: 'n1', type: 'actionNode', position: { x: 0, y: 0 }, data: { blockName: 'A', block_name_mql: 'a', category: 'c', params: {}, enabled: true, id_by_user: 1 } },
            { id: 'n2', type: 'actionNode', position: { x: 0, y: 0 }, data: { blockName: 'B', block_name_mql: 'b', category: 'c', params: {}, enabled: true, id_by_user: 2 } },
          ],
          edges: [],
        },
      },
    });

    useEditorStore.getState().updateNodeData('n1', { enabled: false });
    const nodes = useEditorStore.getState().eventGraphs.on_tick.nodes;
    expect(nodes[0].data.enabled).toBe(false);
    expect(nodes[1].data.enabled).toBe(true); // Unchanged
  });

  it('sets and clears selected node', () => {
    useEditorStore.getState().setSelectedNode('n1');
    expect(useEditorStore.getState().selectedNodeId).toBe('n1');
    useEditorStore.getState().setSelectedNode(null);
    expect(useEditorStore.getState().selectedNodeId).toBeNull();
  });

  it('loads strategy replaces all event graphs', () => {
    const newGraphs = {
      on_tick: {
        nodes: [{ id: 'loaded-1', type: 'actionNode', position: { x: 50, y: 50 }, data: { blockName: 'Loaded', block_name_mql: 'loaded', category: 'test', params: {}, enabled: true, id_by_user: 99 } }],
        edges: [],
      },
      on_init: { nodes: [], edges: [] },
      on_timer: { nodes: [], edges: [] },
      on_trade: { nodes: [], edges: [] },
      on_chart: { nodes: [], edges: [] },
      on_deinit: { nodes: [], edges: [] },
    };
    useEditorStore.getState().loadStrategy(newGraphs as any);
    expect(useEditorStore.getState().eventGraphs.on_tick.nodes).toHaveLength(1);
    expect(useEditorStore.getState().eventGraphs.on_tick.nodes[0].id).toBe('loaded-1');
  });

  it('loadStrategy clears selectedNodeId', () => {
    useEditorStore.setState({ selectedNodeId: 'old-node' });
    const newGraphs = {
      on_tick: { nodes: [], edges: [] },
      on_init: { nodes: [], edges: [] },
      on_timer: { nodes: [], edges: [] },
      on_trade: { nodes: [], edges: [] },
      on_chart: { nodes: [], edges: [] },
      on_deinit: { nodes: [], edges: [] },
    };
    useEditorStore.getState().loadStrategy(newGraphs as any);
    expect(useEditorStore.getState().selectedNodeId).toBeNull();
  });

  it('adds nodes to the active event only', () => {
    useEditorStore.getState().setActiveEvent('on_init');
    const node = {
      id: 'init-node',
      type: 'actionNode',
      position: { x: 0, y: 0 },
      data: { blockName: 'Init', block_name_mql: 'init', category: 'c', params: {}, enabled: true, id_by_user: 0 },
    };
    useEditorStore.getState().addNode(node);
    expect(useEditorStore.getState().eventGraphs.on_init.nodes).toHaveLength(1);
    expect(useEditorStore.getState().eventGraphs.on_tick.nodes).toHaveLength(0);
  });

  it('removes nodes from the active event only', () => {
    // Add a node to on_tick
    useEditorStore.setState({
      eventGraphs: {
        ...useEditorStore.getState().eventGraphs,
        on_tick: {
          nodes: [
            { id: 'tick-n1', type: 'actionNode', position: { x: 0, y: 0 }, data: { blockName: 'A', block_name_mql: 'a', category: 'c', params: {}, enabled: true, id_by_user: 1 } },
          ],
          edges: [],
        },
        on_init: {
          nodes: [
            { id: 'init-n1', type: 'actionNode', position: { x: 0, y: 0 }, data: { blockName: 'B', block_name_mql: 'b', category: 'c', params: {}, enabled: true, id_by_user: 2 } },
          ],
          edges: [],
        },
      },
    });

    // Active event is on_tick, remove from on_tick
    useEditorStore.getState().removeNode('tick-n1');
    expect(useEditorStore.getState().eventGraphs.on_tick.nodes).toHaveLength(0);
    // on_init should be untouched
    expect(useEditorStore.getState().eventGraphs.on_init.nodes).toHaveLength(1);
  });

  it('nodes() returns nodes for the active event', () => {
    useEditorStore.setState({
      eventGraphs: {
        ...useEditorStore.getState().eventGraphs,
        on_tick: {
          nodes: [
            { id: 'tick-1', type: 'actionNode', position: { x: 0, y: 0 }, data: { blockName: 'T', block_name_mql: 't', category: 'c', params: {}, enabled: true, id_by_user: 1 } },
          ],
          edges: [],
        },
        on_init: {
          nodes: [
            { id: 'init-1', type: 'actionNode', position: { x: 0, y: 0 }, data: { blockName: 'I', block_name_mql: 'i', category: 'c', params: {}, enabled: true, id_by_user: 2 } },
          ],
          edges: [],
        },
      },
    });

    expect(useEditorStore.getState().nodes()).toHaveLength(1);
    expect(useEditorStore.getState().nodes()[0].id).toBe('tick-1');

    useEditorStore.getState().setActiveEvent('on_init');
    expect(useEditorStore.getState().nodes()).toHaveLength(1);
    expect(useEditorStore.getState().nodes()[0].id).toBe('init-1');
  });

  it('edges() returns edges for the active event', () => {
    useEditorStore.setState({
      eventGraphs: {
        ...useEditorStore.getState().eventGraphs,
        on_tick: {
          nodes: [],
          edges: [{ id: 'e-tick', source: 'a', target: 'b', type: 'conditionalEdge' }],
        },
        on_init: {
          nodes: [],
          edges: [{ id: 'e-init', source: 'c', target: 'd', type: 'conditionalEdge' }],
        },
      },
    });

    expect(useEditorStore.getState().edges()).toHaveLength(1);
    expect(useEditorStore.getState().edges()[0].id).toBe('e-tick');

    useEditorStore.getState().setActiveEvent('on_init');
    expect(useEditorStore.getState().edges()).toHaveLength(1);
    expect(useEditorStore.getState().edges()[0].id).toBe('e-init');
  });
});
