import { useState } from 'react';
import { generateAiStrategy } from '../../api/generate';
import { useEditorStore, type EventGraphData } from '../../stores/editorStore';
import { useStrategyStore } from '../../stores/strategyStore';
import type { EventName } from '../../types';

interface AiChatProps {
  onClose: () => void;
}

function getNodeType(block_name_mql: string): string {
  if (['buy_now', 'sell_now', 'close_trade_in_loop', 'trailing_stop'].includes(block_name_mql)) return 'actionNode';
  if (block_name_mql === 'condition') return 'conditionNode';
  if (['once_per_bar', 'time_filter', 'spread_filter', 'check_trades_count'].includes(block_name_mql)) return 'filterNode';
  if (block_name_mql === 'loop_for_trades') return 'loopNode';
  if (['and_gate', 'or_gate', 'pass'].includes(block_name_mql)) return 'controlNode';
  return 'actionNode';
}

const EVENT_NAMES: EventName[] = ['on_tick', 'on_init', 'on_timer', 'on_trade', 'on_chart', 'on_deinit'];

export function AiChat({ onClose }: AiChatProps) {
  const [prompt, setPrompt] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [success, setSuccess] = useState(false);

  const loadStrategy = useEditorStore((s) => s.loadStrategy);
  const { setVariables, setConstants, setProjectOptions } = useStrategyStore();

  const handleSubmit = async () => {
    if (!prompt.trim()) return;
    setLoading(true);
    setError(null);
    setSuccess(false);

    try {
      const result = await generateAiStrategy(prompt);
      const strategy = result.strategy;

      // Convert to React Flow format
      const eventGraphs: Record<EventName, EventGraphData> = {
        on_tick: { nodes: [], edges: [] },
        on_init: { nodes: [], edges: [] },
        on_timer: { nodes: [], edges: [] },
        on_trade: { nodes: [], edges: [] },
        on_chart: { nodes: [], edges: [] },
        on_deinit: { nodes: [], edges: [] },
      };

      for (const eventName of EVENT_NAMES) {
        const eventData = strategy.events?.[eventName];
        if (!eventData) continue;

        eventGraphs[eventName] = {
          nodes: (eventData.nodes || []).map((n: any) => ({
            id: n.id,
            type: getNodeType(n.block_name_mql),
            position: n.position || { x: 0, y: 0 },
            data: {
              blockName: n.blockName,
              block_name_mql: n.block_name_mql,
              category: n.category,
              params: n.params || {},
              enabled: n.enabled ?? true,
              id_by_user: n.id_by_user || 0,
            },
          })),
          edges: (eventData.edges || []).map((e: any) => ({
            id: e.id || `edge-${Date.now()}-${Math.random()}`,
            source: e.source,
            sourceHandle: e.sourceHandle || 'blue',
            target: e.target,
            targetHandle: e.targetHandle || 'c',
            type: 'conditionalEdge',
          })),
        };
      }

      loadStrategy(eventGraphs);

      if (strategy.variables) setVariables(strategy.variables);
      if (strategy.constants) setConstants(strategy.constants);
      if (strategy.project_options) setProjectOptions(strategy.project_options);

      setSuccess(true);
    } catch (e: any) {
      setError(e.message || 'AI generation failed');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div
      className="fixed right-0 top-12 bottom-0 w-96 z-40 border-l shadow-2xl flex flex-col"
      style={{ backgroundColor: 'var(--color-surface)', borderColor: 'var(--color-border)' }}
    >
      {/* Header */}
      <div
        className="flex items-center justify-between px-4 py-3 border-b"
        style={{ borderColor: 'var(--color-border)' }}
      >
        <h2 className="text-sm font-semibold" style={{ color: 'var(--color-text)' }}>AI Strategy Assistant</h2>
        <button onClick={onClose} className="text-sm" style={{ color: 'var(--color-text-muted)' }}>Close</button>
      </div>

      {/* Body */}
      <div className="flex-1 p-4 overflow-y-auto">
        <p className="text-xs mb-4" style={{ color: 'var(--color-text-muted)' }}>
          Describe your trading strategy in plain English. The AI will generate a node graph for you.
        </p>

        {error && (
          <div className="mb-3 p-2 rounded text-xs" style={{ backgroundColor: '#ef444420', color: '#ef4444' }}>
            {error}
          </div>
        )}

        {success && (
          <div className="mb-3 p-2 rounded text-xs" style={{ backgroundColor: '#22c55e20', color: '#22c55e' }}>
            Strategy loaded onto canvas!
          </div>
        )}

        <textarea
          value={prompt}
          onChange={(e) => setPrompt(e.target.value)}
          placeholder="e.g., Buy when RSI crosses above 70 with a 50 pip stop loss, only once per bar..."
          rows={6}
          className="w-full text-sm px-3 py-2 rounded border resize-none mb-3"
          style={{ backgroundColor: 'var(--color-surface-light)', borderColor: 'var(--color-border)', color: 'var(--color-text)' }}
        />

        <button
          onClick={handleSubmit}
          disabled={loading || !prompt.trim()}
          className="w-full py-2 text-sm font-medium text-white rounded disabled:opacity-50"
          style={{ backgroundColor: 'var(--color-primary)' }}
        >
          {loading ? 'Generating strategy...' : 'Generate Strategy'}
        </button>
      </div>
    </div>
  );
}
