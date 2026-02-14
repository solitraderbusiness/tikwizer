import { describe, it, expect, beforeEach } from 'vitest';
import { serializeStrategy } from './serializer';
import { useEditorStore } from '../stores/editorStore';
import { useStrategyStore } from '../stores/strategyStore';

describe('serializeStrategy', () => {
  beforeEach(() => {
    // Reset stores to defaults
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

    useStrategyStore.setState({
      name: 'New Strategy',
      variables: [],
      constants: [],
    });
  });

  it('returns all 6 event types', () => {
    const result = serializeStrategy();
    expect(result.events).toBeDefined();
    expect(Object.keys(result.events)).toHaveLength(6);
    expect(result.events.on_tick).toBeDefined();
    expect(result.events.on_init).toBeDefined();
    expect(result.events.on_timer).toBeDefined();
    expect(result.events.on_trade).toBeDefined();
    expect(result.events.on_chart).toBeDefined();
    expect(result.events.on_deinit).toBeDefined();
  });

  it('returns empty arrays for events with no nodes', () => {
    const result = serializeStrategy();
    expect(result.events.on_tick.nodes).toEqual([]);
    expect(result.events.on_tick.edges).toEqual([]);
  });

  it('returns empty arrays for all events when graphs are empty', () => {
    const result = serializeStrategy();
    const eventNames = ['on_tick', 'on_init', 'on_timer', 'on_trade', 'on_chart', 'on_deinit'] as const;
    for (const name of eventNames) {
      expect(result.events[name].nodes).toEqual([]);
      expect(result.events[name].edges).toEqual([]);
    }
  });

  it('serializes nodes correctly', () => {
    useEditorStore.setState({
      eventGraphs: {
        ...useEditorStore.getState().eventGraphs,
        on_tick: {
          nodes: [
            {
              id: 'test-node-1',
              type: 'actionNode',
              position: { x: 100, y: 200 },
              data: {
                blockName: 'Buy Now',
                block_name_mql: 'buy_now',
                category: 'buy_sell',
                params: { lot_size: '0.01' },
                enabled: true,
                id_by_user: 1,
              },
            },
          ],
          edges: [],
        },
      },
    });

    const result = serializeStrategy();
    const node = result.events.on_tick.nodes[0];
    expect(node.id).toBe('test-node-1');
    expect(node.id_by_user).toBe(1);
    expect(node.blockName).toBe('Buy Now');
    expect(node.block_name_mql).toBe('buy_now');
    expect(node.category).toBe('buy_sell');
    expect(node.params.lot_size).toBe('0.01');
    expect(node.enabled).toBe(true);
    expect(node.position).toEqual({ x: 100, y: 200 });
  });

  it('serializes multiple nodes in the same event', () => {
    useEditorStore.setState({
      eventGraphs: {
        ...useEditorStore.getState().eventGraphs,
        on_tick: {
          nodes: [
            {
              id: 'node-1',
              type: 'actionNode',
              position: { x: 0, y: 0 },
              data: { blockName: 'A', block_name_mql: 'a', category: 'c1', params: {}, enabled: true, id_by_user: 1 },
            },
            {
              id: 'node-2',
              type: 'actionNode',
              position: { x: 100, y: 100 },
              data: { blockName: 'B', block_name_mql: 'b', category: 'c2', params: {}, enabled: false, id_by_user: 2 },
            },
          ],
          edges: [],
        },
      },
    });

    const result = serializeStrategy();
    expect(result.events.on_tick.nodes).toHaveLength(2);
    expect(result.events.on_tick.nodes[0].id).toBe('node-1');
    expect(result.events.on_tick.nodes[1].id).toBe('node-2');
    expect(result.events.on_tick.nodes[1].enabled).toBe(false);
  });

  it('serializes edges correctly', () => {
    useEditorStore.setState({
      eventGraphs: {
        ...useEditorStore.getState().eventGraphs,
        on_tick: {
          nodes: [],
          edges: [
            {
              id: 'edge-1',
              source: 'node-a',
              target: 'node-b',
              sourceHandle: 'blue',
              targetHandle: 'c',
              type: 'conditionalEdge',
            },
          ],
        },
      },
    });

    const result = serializeStrategy();
    const edge = result.events.on_tick.edges[0];
    expect(edge.id).toBe('edge-1');
    expect(edge.source).toBe('node-a');
    expect(edge.target).toBe('node-b');
    expect(edge.sourceHandle).toBe('blue');
    expect(edge.targetHandle).toBe('c');
    // serializer always outputs type as 'customEdge'
    expect(edge.type).toBe('customEdge');
  });

  it('defaults sourceHandle to blue and targetHandle to c when missing', () => {
    useEditorStore.setState({
      eventGraphs: {
        ...useEditorStore.getState().eventGraphs,
        on_tick: {
          nodes: [],
          edges: [
            {
              id: 'edge-no-handles',
              source: 'node-x',
              target: 'node-y',
              type: 'conditionalEdge',
            },
          ],
        },
      },
    });

    const result = serializeStrategy();
    const edge = result.events.on_tick.edges[0];
    expect(edge.sourceHandle).toBe('blue');
    expect(edge.targetHandle).toBe('c');
  });

  it('serializes nodes in different events independently', () => {
    useEditorStore.setState({
      eventGraphs: {
        ...useEditorStore.getState().eventGraphs,
        on_tick: {
          nodes: [
            { id: 'tick-1', type: 'actionNode', position: { x: 0, y: 0 }, data: { blockName: 'Tick', block_name_mql: 'tick', category: 'c', params: {}, enabled: true, id_by_user: 1 } },
          ],
          edges: [],
        },
        on_init: {
          nodes: [
            { id: 'init-1', type: 'actionNode', position: { x: 50, y: 50 }, data: { blockName: 'Init', block_name_mql: 'init', category: 'c', params: {}, enabled: true, id_by_user: 2 } },
          ],
          edges: [],
        },
      },
    });

    const result = serializeStrategy();
    expect(result.events.on_tick.nodes).toHaveLength(1);
    expect(result.events.on_tick.nodes[0].id).toBe('tick-1');
    expect(result.events.on_init.nodes).toHaveLength(1);
    expect(result.events.on_init.nodes[0].id).toBe('init-1');
    expect(result.events.on_timer.nodes).toHaveLength(0);
  });

  it('defaults node params to empty object when params is falsy', () => {
    useEditorStore.setState({
      eventGraphs: {
        ...useEditorStore.getState().eventGraphs,
        on_tick: {
          nodes: [
            {
              id: 'no-params',
              type: 'actionNode',
              position: { x: 0, y: 0 },
              data: { blockName: 'NP', block_name_mql: 'np', category: 'c', params: undefined as any, enabled: true, id_by_user: 1 },
            },
          ],
          edges: [],
        },
      },
    });

    const result = serializeStrategy();
    expect(result.events.on_tick.nodes[0].params).toEqual({});
  });

  it('includes strategy metadata', () => {
    const testVars = [{ id: 'v1', type: 'double', name: 'myVar', value: '0', description: '' }];
    useStrategyStore.setState({ variables: testVars });

    const result = serializeStrategy();
    expect(result.variables).toEqual(testVars);
    expect(result.constants).toBeDefined();
    expect(result.project_options).toBeDefined();
  });

  it('includes constants from strategy store', () => {
    const testConsts = [{ id: 'c1', type: 'int', name: 'MAX', value: '100', description: 'max val' }];
    useStrategyStore.setState({ constants: testConsts });

    const result = serializeStrategy();
    expect(result.constants).toEqual(testConsts);
  });

  it('includes project_options with defaults', () => {
    const result = serializeStrategy();
    expect(result.project_options.magic_and_other.magic_number).toBe('55225');
    expect(result.project_options.magic_and_other.on_timer_period).toBe('600');
    expect(result.project_options.virtual_stops.virtual_stops).toBe('True');
    expect(result.project_options.virtual_stops.add_pips).toBe('100');
    expect(result.project_options.description_and_version_number.version_number).toBe('1.0');
    expect(result.project_options.visual.display_spread_meter).toBe('True');
  });
});
