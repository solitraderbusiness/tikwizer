const INDICATORS = [
  'rsi', 'ma', 'macd', 'bollinger_band', 'stochastic', 'cci', 'atr', 'adx',
  'momentum', 'rvi', 'mfi', 'wpr', 'demarker', 'force', 'obv',
  'alligator', 'ichimoku', 'parabolic_sar', 'envelopes', 'fractals',
  'awesome_oscillator', 'accelerator_oscillator', 'bears_power', 'bulls_power',
  'gator', 'osma', 'stddev', 'accumulation_distribution', 'market_facilitation',
  'zigzag', 'profit_unrealized', 'custom',
];

interface IndicatorSelectorProps {
  selectedIndicator: string;
  params: Record<string, any>;
  onChange: (indicator: string, params: Record<string, any>) => void;
}

export function IndicatorSelector({ selectedIndicator, params, onChange }: IndicatorSelectorProps) {
  return (
    <div className="space-y-2">
      <div>
        <label className="block text-xs mb-1" style={{ color: 'var(--color-text-muted)' }}>Indicator</label>
        <select
          value={selectedIndicator}
          onChange={(e) => onChange(e.target.value, {})}
          className="w-full text-sm px-2 py-1.5 rounded border"
          style={{ backgroundColor: 'var(--color-surface-light)', borderColor: 'var(--color-border)', color: 'var(--color-text)' }}
        >
          {INDICATORS.map((ind) => (
            <option key={ind} value={ind}>{ind.replace(/_/g, ' ').replace(/\b\w/g, (c) => c.toUpperCase())}</option>
          ))}
        </select>
      </div>

      <div>
        <label className="block text-xs mb-1" style={{ color: 'var(--color-text-muted)' }}>Period</label>
        <input
          type="text"
          value={params.period || '14'}
          onChange={(e) => onChange(selectedIndicator, { ...params, period: e.target.value })}
          className="w-full text-sm px-2 py-1.5 rounded border"
          style={{ backgroundColor: 'var(--color-surface-light)', borderColor: 'var(--color-border)', color: 'var(--color-text)' }}
        />
      </div>

      <div>
        <label className="block text-xs mb-1" style={{ color: 'var(--color-text-muted)' }}>Applied Price</label>
        <select
          value={params.applied_price || 'PRICE_CLOSE'}
          onChange={(e) => onChange(selectedIndicator, { ...params, applied_price: e.target.value })}
          className="w-full text-sm px-2 py-1.5 rounded border"
          style={{ backgroundColor: 'var(--color-surface-light)', borderColor: 'var(--color-border)', color: 'var(--color-text)' }}
        >
          <option value="PRICE_CLOSE">Close</option>
          <option value="PRICE_OPEN">Open</option>
          <option value="PRICE_HIGH">High</option>
          <option value="PRICE_LOW">Low</option>
          <option value="PRICE_MEDIAN">Median</option>
          <option value="PRICE_TYPICAL">Typical</option>
          <option value="PRICE_WEIGHTED">Weighted</option>
        </select>
      </div>

      <div>
        <label className="block text-xs mb-1" style={{ color: 'var(--color-text-muted)' }}>Shift</label>
        <input
          type="text"
          value={params.shift || '0'}
          onChange={(e) => onChange(selectedIndicator, { ...params, shift: e.target.value })}
          className="w-full text-sm px-2 py-1.5 rounded border"
          style={{ backgroundColor: 'var(--color-surface-light)', borderColor: 'var(--color-border)', color: 'var(--color-text)' }}
        />
      </div>

      <div>
        <label className="block text-xs mb-1" style={{ color: 'var(--color-text-muted)' }}>Symbol</label>
        <input
          type="text"
          value={params.Symbol || ''}
          onChange={(e) => onChange(selectedIndicator, { ...params, Symbol: e.target.value })}
          placeholder="Leave empty for current"
          className="w-full text-sm px-2 py-1.5 rounded border"
          style={{ backgroundColor: 'var(--color-surface-light)', borderColor: 'var(--color-border)', color: 'var(--color-text)' }}
        />
      </div>

      <div>
        <label className="block text-xs mb-1" style={{ color: 'var(--color-text-muted)' }}>Timeframe</label>
        <select
          value={params.Period || 'PERIOD_CURRENT'}
          onChange={(e) => onChange(selectedIndicator, { ...params, Period: e.target.value })}
          className="w-full text-sm px-2 py-1.5 rounded border"
          style={{ backgroundColor: 'var(--color-surface-light)', borderColor: 'var(--color-border)', color: 'var(--color-text)' }}
        >
          <option value="PERIOD_CURRENT">Current</option>
          <option value="PERIOD_M1">M1</option>
          <option value="PERIOD_M5">M5</option>
          <option value="PERIOD_M15">M15</option>
          <option value="PERIOD_M30">M30</option>
          <option value="PERIOD_H1">H1</option>
          <option value="PERIOD_H4">H4</option>
          <option value="PERIOD_D1">D1</option>
          <option value="PERIOD_W1">W1</option>
          <option value="PERIOD_MN1">MN1</option>
        </select>
      </div>
    </div>
  );
}
