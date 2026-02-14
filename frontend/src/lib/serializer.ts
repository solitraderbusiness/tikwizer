import { useEditorStore } from '../stores/editorStore';
import { useStrategyStore } from '../stores/strategyStore';
import type { StrategyData, EventName } from '../types';

const EVENT_NAMES: EventName[] = ['on_tick', 'on_init', 'on_timer', 'on_trade', 'on_chart', 'on_deinit'];

export function serializeStrategy(): StrategyData {
  const editorState = useEditorStore.getState();
  const strategyState = useStrategyStore.getState();

  const events: Record<string, any> = {};

  for (const eventName of EVENT_NAMES) {
    const graph = editorState.eventGraphs[eventName];
    events[eventName] = {
      nodes: graph.nodes.map((node) => ({
        id: node.id,
        id_by_user: node.data.id_by_user,
        blockName: node.data.blockName,
        block_name_mql: node.data.block_name_mql,
        category: node.data.category,
        params: node.data.params || {},
        enabled: node.data.enabled,
        position: node.position,
      })),
      edges: graph.edges.map((edge) => ({
        id: edge.id,
        source: edge.source,
        sourceHandle: edge.sourceHandle || 'blue',
        target: edge.target,
        targetHandle: edge.targetHandle || 'c',
        type: 'customEdge',
      })),
    };
  }

  return {
    events,
    variables: strategyState.variables,
    constants: strategyState.constants,
    project_options: strategyState.projectOptions,
  } as StrategyData;
}
