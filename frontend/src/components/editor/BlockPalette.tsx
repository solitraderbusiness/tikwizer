import { type DragEvent, useEffect, useState } from 'react';
import { getBlocks } from '../../api/generate';
import type { BlockCategory, EventName } from '../../types';
import { useEditorStore } from '../../stores/editorStore';
import { useStrategyStore } from '../../stores/strategyStore';
import { uid } from '../../lib/uid';

interface PaletteBlock {
  blockName: string;
  block_name_mql: string;
  category: string;
  nodeType: string;
  default_params: Record<string, any>;
}

interface PaletteCategory {
  label: string;
  categoryKey: string;
  blocks: PaletteBlock[];
}

/** Map backend category names to React Flow node types */
const CATEGORY_NODE_TYPE: Record<string, string> = {
  buy_sell: 'actionNode',
  chart_objects: 'actionNode',
  check_trades_orders_count: 'conditionNode',
  check_trading_conditions: 'conditionNode',
  condition_formula: 'conditionNode',
  controlling_blocks: 'controlNode',
  counters: 'controlNode',
  loop_for_chart_objects: 'loopNode',
  loop_for_trades_orders: 'loopNode',
  more: 'controlNode',
  on_chart_filter_specific_event: 'filterNode',
  on_timer_filter_specific_event: 'filterNode',
  on_trade_filter_specific_event: 'filterNode',
  output_communication: 'actionNode',
  time_filters: 'filterNode',
  trading_actions: 'actionNode',
  trailing_stop_break_even: 'actionNode',
  variables: 'actionNode',
  various_signals: 'conditionNode',
};

/** Make category names more readable */
const CATEGORY_LABELS: Record<string, string> = {
  buy_sell: 'Buy / Sell',
  chart_objects: 'Chart Objects',
  check_trades_orders_count: 'Check Trades Count',
  check_trading_conditions: 'Check Trading Conditions',
  condition_formula: 'Conditions & Formulas',
  controlling_blocks: 'Controlling Blocks',
  counters: 'Counters',
  loop_for_chart_objects: 'Loop: Chart Objects',
  loop_for_trades_orders: 'Loop: Trades & Orders',
  more: 'More',
  on_chart_filter_specific_event: 'On Chart Events',
  on_timer_filter_specific_event: 'On Timer Events',
  on_trade_filter_specific_event: 'On Trade Events',
  output_communication: 'Output & Communication',
  time_filters: 'Time Filters',
  trading_actions: 'Trading Actions',
  trailing_stop_break_even: 'Trailing Stop & Break Even',
  variables: 'Variables',
  various_signals: 'Various Signals',
};

/**
 * Categories restricted to specific events.
 * If a category is not listed here, it appears in all events.
 */
const CATEGORY_EVENT_RESTRICTION: Record<string, EventName[]> = {
  on_trade_filter_specific_event: ['on_trade'],
  on_chart_filter_specific_event: ['on_chart'],
  on_timer_filter_specific_event: ['on_timer'],
  // Trading blocks only make sense in on_tick
  buy_sell: ['on_tick'],
  trading_actions: ['on_tick'],
  trailing_stop_break_even: ['on_tick'],
  loop_for_trades_orders: ['on_tick', 'on_trade'],
  check_trades_orders_count: ['on_tick', 'on_trade'],
  check_trading_conditions: ['on_tick', 'on_trade'],
  // Chart object loops only in on_tick and on_chart
  loop_for_chart_objects: ['on_tick', 'on_chart'],
  chart_objects: ['on_tick', 'on_chart'],
};

function convertApiBlocks(apiCategories: BlockCategory[]): PaletteCategory[] {
  return apiCategories
    .filter((cat) => cat.blocks.length > 0)
    .map((cat) => ({
      label: CATEGORY_LABELS[cat.category] || cat.category.replace(/_/g, ' ').replace(/\b\w/g, (c) => c.toUpperCase()),
      categoryKey: cat.category,
      blocks: cat.blocks.map((block) => ({
        blockName: block.display_name,
        block_name_mql: block.name,
        category: cat.category,
        nodeType: CATEGORY_NODE_TYPE[cat.category] || 'controlNode',
        default_params: block.default_params,
      })),
    }));
}

function onDragStart(event: DragEvent, block: PaletteBlock) {
  event.dataTransfer.setData('application/tikwizer-block', JSON.stringify(block));
  event.dataTransfer.effectAllowed = 'move';
}

export function BlockPalette() {
  const [catalog, setCatalog] = useState<PaletteCategory[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [search, setSearch] = useState('');
  const [collapsed, setCollapsed] = useState<Set<string>>(new Set());
  const activeEvent = useEditorStore((s) => s.activeEvent);
  const setSelectedNode = useEditorStore((s) => s.setSelectedNode);

  const constants = useStrategyStore((s) => s.constants);
  const addConstant = useStrategyStore((s) => s.addConstant);
  const variables = useStrategyStore((s) => s.variables);
  const addVariable = useStrategyStore((s) => s.addVariable);
  const selectedVarConst = useStrategyStore((s) => s.selectedVarConst);
  const selectVarConst = useStrategyStore((s) => s.selectVarConst);

  useEffect(() => {
    getBlocks()
      .then((data) => {
        setCatalog(convertApiBlocks(data));
        setLoading(false);
      })
      .catch((err) => {
        setError(err.message);
        setLoading(false);
      });
  }, []);

  const toggleCategory = (label: string) => {
    setCollapsed((prev) => {
      const next = new Set(prev);
      if (next.has(label)) next.delete(label);
      else next.add(label);
      return next;
    });
  };

  // Filter by active event first, then by search
  const eventFiltered = catalog.filter((cat) => {
    const restriction = CATEGORY_EVENT_RESTRICTION[cat.categoryKey];
    return !restriction || restriction.includes(activeEvent);
  });

  const isSearching = search.trim().length > 0;
  const filtered = isSearching
    ? eventFiltered
        .map((cat) => ({
          ...cat,
          blocks: cat.blocks.filter(
            (b) =>
              b.blockName.toLowerCase().includes(search.toLowerCase()) ||
              b.block_name_mql.toLowerCase().includes(search.toLowerCase())
          ),
        }))
        .filter((cat) => cat.blocks.length > 0)
    : eventFiltered;

  return (
    <div
      className="w-60 overflow-y-auto border-r flex-shrink-0"
      style={{ backgroundColor: 'var(--color-surface)', borderColor: 'var(--color-border)' }}
    >
      <div className="p-3">
        <h2 className="text-sm font-semibold mb-2" style={{ color: 'var(--color-text-muted)' }}>
          Blocks
        </h2>

        <input
          type="text"
          placeholder="Search blocks..."
          value={search}
          onChange={(e) => setSearch(e.target.value)}
          className="w-full px-2 py-1.5 mb-3 rounded border text-sm outline-none"
          style={{
            backgroundColor: 'var(--color-surface-light)',
            borderColor: 'var(--color-border)',
            color: 'var(--color-text)',
          }}
        />

        {/* Constants */}
        <div className="mb-3">
          <div className="flex items-center justify-between mb-1.5">
            <button
              onClick={() => toggleCategory('__constants')}
              className="flex items-center gap-1 text-xs font-medium uppercase tracking-wide"
              style={{ color: 'var(--color-text-muted)' }}
            >
              <span className="text-[10px]">{collapsed.has('__constants') ? '\u25B6' : '\u25BC'}</span>
              Constants
              <span className="text-[10px] font-normal normal-case ml-1">{constants.length}</span>
            </button>
            <button
              onClick={() => {
                const newConst = { id: uid(), type: 'double', name: '', value: '', description: '' };
                addConstant(newConst);
                setSelectedNode(null);
                selectVarConst({ kind: 'constant', id: newConst.id });
              }}
              className="text-[10px] px-1.5 py-0.5 rounded"
              style={{ backgroundColor: 'var(--color-primary)', color: 'white' }}
            >
              + Add
            </button>
          </div>
          {!collapsed.has('__constants') && (
            <div className="space-y-1">
              {constants.map((c) => (
                <div
                  key={c.id}
                  onClick={() => {
                    setSelectedNode(null);
                    selectVarConst({ kind: 'constant', id: c.id });
                  }}
                  className="px-3 py-2 rounded text-sm cursor-pointer border transition-colors"
                  style={{
                    backgroundColor: selectedVarConst?.kind === 'constant' && selectedVarConst.id === c.id
                      ? 'var(--color-primary)' : 'var(--color-surface-light)',
                    borderColor: selectedVarConst?.kind === 'constant' && selectedVarConst.id === c.id
                      ? 'var(--color-primary)' : 'var(--color-border)',
                    color: selectedVarConst?.kind === 'constant' && selectedVarConst.id === c.id
                      ? 'white' : 'var(--color-text)',
                  }}
                >
                  <div className="truncate">{c.name || '(unnamed)'}</div>
                  <div className="text-[10px] opacity-70">{c.type} = {c.value || '?'}</div>
                </div>
              ))}
            </div>
          )}
        </div>

        {/* Variables */}
        <div className="mb-3">
          <div className="flex items-center justify-between mb-1.5">
            <button
              onClick={() => toggleCategory('__variables')}
              className="flex items-center gap-1 text-xs font-medium uppercase tracking-wide"
              style={{ color: 'var(--color-text-muted)' }}
            >
              <span className="text-[10px]">{collapsed.has('__variables') ? '\u25B6' : '\u25BC'}</span>
              Variables
              <span className="text-[10px] font-normal normal-case ml-1">{variables.length}</span>
            </button>
            <button
              onClick={() => {
                const newVar = { id: uid(), type: 'double', name: '', value: '', description: '' };
                addVariable(newVar);
                setSelectedNode(null);
                selectVarConst({ kind: 'variable', id: newVar.id });
              }}
              className="text-[10px] px-1.5 py-0.5 rounded"
              style={{ backgroundColor: 'var(--color-primary)', color: 'white' }}
            >
              + Add
            </button>
          </div>
          {!collapsed.has('__variables') && (
            <div className="space-y-1">
              {variables.map((v) => (
                <div
                  key={v.id}
                  onClick={() => {
                    setSelectedNode(null);
                    selectVarConst({ kind: 'variable', id: v.id });
                  }}
                  className="px-3 py-2 rounded text-sm cursor-pointer border transition-colors"
                  style={{
                    backgroundColor: selectedVarConst?.kind === 'variable' && selectedVarConst.id === v.id
                      ? 'var(--color-primary)' : 'var(--color-surface-light)',
                    borderColor: selectedVarConst?.kind === 'variable' && selectedVarConst.id === v.id
                      ? 'var(--color-primary)' : 'var(--color-border)',
                    color: selectedVarConst?.kind === 'variable' && selectedVarConst.id === v.id
                      ? 'white' : 'var(--color-text)',
                  }}
                >
                  <div className="truncate">{v.name || '(unnamed)'}</div>
                  <div className="text-[10px] opacity-70">{v.type} = {v.value || '?'}</div>
                </div>
              ))}
            </div>
          )}
        </div>

        <div className="border-t mb-3" style={{ borderColor: 'var(--color-border)' }} />

        {loading && (
          <p className="text-xs" style={{ color: 'var(--color-text-muted)' }}>Loading blocks...</p>
        )}
        {error && (
          <p className="text-xs" style={{ color: 'var(--color-accent-red)' }}>Error: {error}</p>
        )}

        {filtered.map((cat) => (
          <div key={cat.label} className="mb-3">
            <button
              onClick={() => toggleCategory(cat.label)}
              className="flex items-center gap-1 w-full text-left text-xs font-medium mb-1.5 uppercase tracking-wide"
              style={{ color: 'var(--color-text-muted)' }}
            >
              <span className="text-[10px]">{!isSearching && collapsed.has(cat.label) ? '\u25B6' : '\u25BC'}</span>
              {cat.label}
              <span className="ml-auto text-[10px] font-normal normal-case">{cat.blocks.length}</span>
            </button>
            {(isSearching || !collapsed.has(cat.label)) && (
              <div className="space-y-1">
                {cat.blocks.map((block) => (
                  <div
                    key={block.block_name_mql}
                    draggable
                    onDragStart={(e) => onDragStart(e, block)}
                    className="px-3 py-2 rounded text-sm cursor-grab active:cursor-grabbing border transition-colors"
                    style={{
                      backgroundColor: 'var(--color-surface-light)',
                      borderColor: 'var(--color-border)',
                      color: 'var(--color-text)',
                    }}
                    onMouseEnter={(e) => {
                      (e.currentTarget as HTMLElement).style.borderColor = 'var(--color-primary)';
                    }}
                    onMouseLeave={(e) => {
                      (e.currentTarget as HTMLElement).style.borderColor = 'var(--color-border)';
                    }}
                  >
                    {block.blockName}
                  </div>
                ))}
              </div>
            )}
          </div>
        ))}
      </div>
    </div>
  );
}
