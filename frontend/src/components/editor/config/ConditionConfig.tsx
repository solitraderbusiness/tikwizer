import { IndicatorSelector } from './IndicatorSelector';

interface ConditionConfigProps {
  params: Record<string, any>;
  onChange: (params: Record<string, any>) => void;
}

const OPERATORS = [
  { value: '>', label: '>' },
  { value: '<', label: '<' },
  { value: '>=', label: '>=' },
  { value: '<=', label: '<=' },
  { value: '==', label: '==' },
  { value: '!=', label: '!=' },
  { value: '×>', label: '×> (Cross Above)' },
  { value: '×<', label: '×< (Cross Below)' },
];

export function ConditionConfig({ params, onChange }: ConditionConfigProps) {
  const operator = params.operator?.label || '>';
  const left = params.left || {};
  const right = params.right || {};

  return (
    <div className="space-y-4">
      {/* Left side */}
      <div>
        <h3 className="text-xs font-semibold mb-2 uppercase tracking-wide" style={{ color: 'var(--color-text-muted)' }}>
          Left Value
        </h3>
        <ValueSideConfig side={left} onChange={(v) => onChange({ left: v })} />
      </div>

      {/* Operator */}
      <div>
        <label className="block text-xs mb-1" style={{ color: 'var(--color-text-muted)' }}>Operator</label>
        <select
          value={operator}
          onChange={(e) => onChange({ operator: { label: e.target.value } })}
          className="w-full text-sm px-2 py-1.5 rounded border"
          style={{ backgroundColor: 'var(--color-surface-light)', borderColor: 'var(--color-border)', color: 'var(--color-text)' }}
        >
          {OPERATORS.map((op) => (
            <option key={op.value} value={op.value}>{op.label}</option>
          ))}
        </select>
      </div>

      {/* Right side */}
      <div>
        <h3 className="text-xs font-semibold mb-2 uppercase tracking-wide" style={{ color: 'var(--color-text-muted)' }}>
          Right Value
        </h3>
        <ValueSideConfig side={right} onChange={(v) => onChange({ right: v })} />
      </div>
    </div>
  );
}

function ValueSideConfig({ side, onChange }: { side: Record<string, any>; onChange: (v: Record<string, any>) => void }) {
  const row1 = side.row1 || 'value';
  const row2 = side.row2 || 'Numeric';
  const sideParams = side.params || {};

  return (
    <div className="space-y-2">
      <div>
        <label className="block text-xs mb-1" style={{ color: 'var(--color-text-muted)' }}>Type</label>
        <select
          value={row1}
          onChange={(e) => onChange({ ...side, row1: e.target.value, params: {} })}
          className="w-full text-sm px-2 py-1.5 rounded border"
          style={{ backgroundColor: 'var(--color-surface-light)', borderColor: 'var(--color-border)', color: 'var(--color-text)' }}
        >
          <option value="indicator">Indicator</option>
          <option value="value">Value</option>
          <option value="candle">Candle</option>
          <option value="market-properties">Market Properties</option>
          <option value="account">Account</option>
        </select>
      </div>

      {row1 === 'indicator' && (
        <IndicatorSelector
          selectedIndicator={row2}
          params={sideParams}
          onChange={(indicator, indicatorParams) => onChange({ ...side, row1: 'indicator', row2: indicator, params: indicatorParams })}
        />
      )}

      {row1 === 'value' && (
        <div>
          <label className="block text-xs mb-1" style={{ color: 'var(--color-text-muted)' }}>Numeric Value</label>
          <input
            type="text"
            value={sideParams.value || ''}
            onChange={(e) => onChange({ ...side, row1: 'value', row2: 'Numeric', params: { ...sideParams, value: e.target.value } })}
            className="w-full text-sm px-2 py-1.5 rounded border"
            style={{ backgroundColor: 'var(--color-surface-light)', borderColor: 'var(--color-border)', color: 'var(--color-text)' }}
          />
        </div>
      )}

      {row1 === 'candle' && (
        <div className="space-y-2">
          <div>
            <label className="block text-xs mb-1" style={{ color: 'var(--color-text-muted)' }}>Candle Property</label>
            <select
              value={sideParams.candle_property || 'close'}
              onChange={(e) => onChange({ ...side, row1: 'candle', row2: 'candle', params: { ...sideParams, candle_property: e.target.value } })}
              className="w-full text-sm px-2 py-1.5 rounded border"
              style={{ backgroundColor: 'var(--color-surface-light)', borderColor: 'var(--color-border)', color: 'var(--color-text)' }}
            >
              <option value="close">Close</option>
              <option value="open">Open</option>
              <option value="high">High</option>
              <option value="low">Low</option>
            </select>
          </div>
          <div>
            <label className="block text-xs mb-1" style={{ color: 'var(--color-text-muted)' }}>Shift</label>
            <input
              type="text"
              value={sideParams.shift || '0'}
              onChange={(e) => onChange({ ...side, row1: 'candle', row2: 'candle', params: { ...sideParams, shift: e.target.value } })}
              className="w-full text-sm px-2 py-1.5 rounded border"
              style={{ backgroundColor: 'var(--color-surface-light)', borderColor: 'var(--color-border)', color: 'var(--color-text)' }}
            />
          </div>
        </div>
      )}
    </div>
  );
}
