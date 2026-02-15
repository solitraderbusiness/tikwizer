import { ParamInput } from './ParamInput';
import { getFieldOptions } from './fieldOptions';

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

      <ParamInput
        label="Money Management"
        value={params.money_management || 'MONEY_MANAGEMENT_FIXED_VOLUME'}
        onChange={(v) => onChange({ money_management: v })}
        options={getFieldOptions('money_management', params.money_management || '') ?? undefined}
      />
      <ParamInput
        label="Volume / Lot Size"
        value={String(params.how_much_volume ?? '0.01')}
        onChange={(v) => onChange({ how_much_volume: v })}
      />
      <ParamInput
        label="Volume Upper Limit"
        value={String(params.volume_upper_limit ?? '0')}
        onChange={(v) => onChange({ volume_upper_limit: v })}
      />
      <ParamInput
        label="Open At Price"
        value={params.open_at_price || 'OPEN_AT_ASK'}
        onChange={(v) => onChange({ open_at_price: v })}
        options={getFieldOptions('open_at_price', params.open_at_price || '') ?? undefined}
      />
      <ParamInput
        label="Price Offset"
        value={String(params.price_offset ?? '0')}
        onChange={(v) => onChange({ price_offset: v })}
      />
      <ParamInput
        label="Price Offset As Pip"
        value={String(params.price_offset_as_pip ?? 'true')}
        onChange={(v) => onChange({ price_offset_as_pip: v })}
        options={getFieldOptions('price_offset_as_pip', String(params.price_offset_as_pip ?? 'true')) ?? undefined}
      />
      <ParamInput
        label="Stop Loss Mode"
        value={params.stop_loss_mode || 'TPSL_MODE_FIXED_PIPS'}
        onChange={(v) => onChange({ stop_loss_mode: v })}
        options={getFieldOptions('stop_loss_mode', params.stop_loss_mode || '') ?? undefined}
      />
      <ParamInput
        label="Stop Loss (pips)"
        value={String(params.stoploss ?? '0')}
        onChange={(v) => onChange({ stoploss: v })}
      />
      <ParamInput
        label="Take Profit Mode"
        value={params.take_profit_mode || 'TPSL_MODE_FIXED_PIPS'}
        onChange={(v) => onChange({ take_profit_mode: v })}
        options={getFieldOptions('take_profit_mode', params.take_profit_mode || '') ?? undefined}
      />
      <ParamInput
        label="Take Profit (pips)"
        value={String(params.takeprofit ?? '0')}
        onChange={(v) => onChange({ takeprofit: v })}
      />
      <ParamInput label="Slippage" value={String(params.slippage ?? '4')} onChange={(v) => onChange({ slippage: v })} />
      <ParamInput label="Comment" value={params.comment || ''} onChange={(v) => onChange({ comment: v })} />
      <ParamInput
        label="Group"
        value={String(params.group ?? '')}
        onChange={(v) => onChange({ group: v })}
      />
      <ParamInput
        label="Expiration (minutes)"
        value={String(params.expiration ?? '0')}
        onChange={(v) => onChange({ expiration: v })}
      />
      <ParamInput
        label="Arrow Color"
        value={params.arrow_color || 'clrYellow'}
        onChange={(v) => onChange({ arrow_color: v })}
        options={getFieldOptions('arrow_color', params.arrow_color || '') ?? undefined}
      />
      <ParamInput
        label="Look Up On"
        value={params.look_up_on || 'LOOK_UP_RUNNING_ONLY'}
        onChange={(v) => onChange({ look_up_on: v })}
        options={getFieldOptions('look_up_on', params.look_up_on || '') ?? undefined}
      />
    </div>
  );
}
