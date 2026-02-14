import { type DragEvent } from 'react';

interface PaletteBlock {
  blockName: string;
  block_name_mql: string;
  category: string;
  nodeType: string; // which custom node component to use
}

interface PaletteCategory {
  label: string;
  blocks: PaletteBlock[];
}

const BLOCK_CATALOG: PaletteCategory[] = [
  {
    label: 'Orders',
    blocks: [
      { blockName: 'Buy Now', block_name_mql: 'buy_now', category: 'buy_sell', nodeType: 'actionNode' },
      { blockName: 'Sell Now', block_name_mql: 'sell_now', category: 'buy_sell', nodeType: 'actionNode' },
    ],
  },
  {
    label: 'Conditions',
    blocks: [
      { blockName: 'Condition', block_name_mql: 'condition', category: 'condition_formula', nodeType: 'conditionNode' },
    ],
  },
  {
    label: 'Filters',
    blocks: [
      { blockName: 'Once Per Bar', block_name_mql: 'once_per_bar', category: 'time_filters', nodeType: 'filterNode' },
      { blockName: 'Time Filter', block_name_mql: 'time_filter', category: 'time_filters', nodeType: 'filterNode' },
      { blockName: 'Spread Filter', block_name_mql: 'spread_filter', category: 'time_filters', nodeType: 'filterNode' },
    ],
  },
  {
    label: 'Loops',
    blocks: [
      { blockName: 'For Each Trade', block_name_mql: 'loop_for_trades', category: 'loop_for_trades_orders', nodeType: 'loopNode' },
    ],
  },
  {
    label: 'Trade Actions',
    blocks: [
      { blockName: 'Close Trade', block_name_mql: 'close_trade_in_loop', category: 'trading_actions', nodeType: 'actionNode' },
      { blockName: 'Trailing Stop', block_name_mql: 'trailing_stop', category: 'trailing_stop_break_even', nodeType: 'actionNode' },
    ],
  },
  {
    label: 'Checks',
    blocks: [
      { blockName: 'Trade Count', block_name_mql: 'check_trades_count', category: 'check_trades_orders_count', nodeType: 'filterNode' },
    ],
  },
  {
    label: 'Logic',
    blocks: [
      { blockName: 'AND', block_name_mql: 'and_gate', category: 'condition_formula', nodeType: 'controlNode' },
      { blockName: 'OR', block_name_mql: 'or_gate', category: 'condition_formula', nodeType: 'controlNode' },
      { blockName: 'Pass', block_name_mql: 'pass', category: 'various_signals', nodeType: 'controlNode' },
    ],
  },
];

function onDragStart(event: DragEvent, block: PaletteBlock) {
  event.dataTransfer.setData('application/tikwizer-block', JSON.stringify(block));
  event.dataTransfer.effectAllowed = 'move';
}

export function BlockPalette() {
  return (
    <div
      className="w-60 overflow-y-auto border-r flex-shrink-0"
      style={{ backgroundColor: 'var(--color-surface)', borderColor: 'var(--color-border)' }}
    >
      <div className="p-3">
        <h2 className="text-sm font-semibold mb-3" style={{ color: 'var(--color-text-muted)' }}>
          Blocks
        </h2>
        {BLOCK_CATALOG.map((cat) => (
          <div key={cat.label} className="mb-4">
            <h3 className="text-xs font-medium mb-1.5 uppercase tracking-wide" style={{ color: 'var(--color-text-muted)' }}>
              {cat.label}
            </h3>
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
          </div>
        ))}
      </div>
    </div>
  );
}
