interface BuySellConfigProps {
  params: Record<string, any>;
  onChange: (params: Record<string, any>) => void;
  isBuy: boolean;
}

export function BuySellConfig({ params, onChange, isBuy }: BuySellConfigProps) {
  return (
    <div className="space-y-3">
      <div className="text-xs font-medium px-2 py-1 rounded inline-block" style={{
        backgroundColor: isBuy ? '#22c55e20' : '#ef444420',
        color: isBuy ? '#22c55e' : '#ef4444',
      }}>
        {isBuy ? 'BUY ORDER' : 'SELL ORDER'}
      </div>

      <Field label="Lot Size" value={params.lot_size || '0.01'} onChange={(v) => onChange({ lot_size: v })} />
      <Field label="Stop Loss (pips)" value={params.stop_loss || '0'} onChange={(v) => onChange({ stop_loss: v })} />
      <Field label="Take Profit (pips)" value={params.take_profit || '0'} onChange={(v) => onChange({ take_profit: v })} />
      <Field label="Slippage" value={params.slippage || '4'} onChange={(v) => onChange({ slippage: v })} />
      <Field label="Comment" value={params.comment || ''} onChange={(v) => onChange({ comment: v })} />
      <Field label="Group" value={params.group || ''} onChange={(v) => onChange({ group: v })} />

      <div>
        <label className="block text-xs mb-1" style={{ color: 'var(--color-text-muted)' }}>Money Management</label>
        <select
          value={params.money_management || 'fixed_lot'}
          onChange={(e) => onChange({ money_management: e.target.value })}
          className="w-full text-sm px-2 py-1.5 rounded border"
          style={{ backgroundColor: 'var(--color-surface-light)', borderColor: 'var(--color-border)', color: 'var(--color-text)' }}
        >
          <option value="fixed_lot">Fixed Lot</option>
          <option value="percent_balance">% of Balance</option>
          <option value="percent_equity">% of Equity</option>
        </select>
      </div>
    </div>
  );
}

function Field({ label, value, onChange }: { label: string; value: string; onChange: (v: string) => void }) {
  return (
    <div>
      <label className="block text-xs mb-1" style={{ color: 'var(--color-text-muted)' }}>{label}</label>
      <input
        type="text"
        value={value}
        onChange={(e) => onChange(e.target.value)}
        className="w-full text-sm px-2 py-1.5 rounded border"
        style={{ backgroundColor: 'var(--color-surface-light)', borderColor: 'var(--color-border)', color: 'var(--color-text)' }}
      />
    </div>
  );
}
