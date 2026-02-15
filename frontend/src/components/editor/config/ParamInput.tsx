import { useState, useRef, useEffect } from 'react';
import { useStrategyStore } from '../../../stores/strategyStore';
import type { FieldOption } from './fieldOptions';

interface ParamInputProps {
  label: string;
  value: string;
  onChange: (value: string) => void;
  placeholder?: string;
  /** When provided, renders a <select> dropdown instead of a text input */
  options?: FieldOption[];
}

/** Variable reference prefix used in param values */
const VAR_PREFIX = '@';

function isVarRef(value: string): boolean {
  return typeof value === 'string' && value.startsWith(VAR_PREFIX);
}

function getVarName(value: string): string {
  return value.slice(VAR_PREFIX.length);
}

/**
 * Infer compatible variable types from a field's current value.
 * - Numbers → int, double
 * - true/false → bool
 * - Strings → string (also allow in numeric fields for enum-like values)
 * If the value is already a variable reference, allow all numeric types.
 */
function getCompatibleTypes(value: string): string[] {
  if (isVarRef(value)) return ['int', 'double', 'string', 'bool'];
  const str = String(value).trim();
  if (str === 'true' || str === 'false' || str === 'True' || str === 'False') {
    return ['bool'];
  }
  if (str !== '' && !isNaN(Number(str))) {
    return ['int', 'double'];
  }
  // String or enum-like values - only allow string vars
  return ['string'];
}

export function ParamInput({ label, value, onChange, placeholder, options }: ParamInputProps) {
  const constants = useStrategyStore((s) => s.constants);
  const variables = useStrategyStore((s) => s.variables);
  const [showDropdown, setShowDropdown] = useState(false);
  const dropdownRef = useRef<HTMLDivElement>(null);

  const strValue = String(value ?? '');
  const isRef = isVarRef(strValue);
  const compatibleTypes = getCompatibleTypes(strValue);

  // All available vars/consts filtered by type compatibility
  const availableItems = [
    ...constants.filter((c) => c.name).map((c) => ({ ...c, kind: 'constant' as const })),
    ...variables.filter((v) => v.name).map((v) => ({ ...v, kind: 'variable' as const })),
  ].filter((item) => compatibleTypes.includes(item.type));

  // If current value is a ref, find the matching item
  const refItem = isRef
    ? [...constants, ...variables].find((item) => item.name === getVarName(strValue))
    : null;

  useEffect(() => {
    if (!showDropdown) return;
    const handleClick = (e: MouseEvent) => {
      if (dropdownRef.current && !dropdownRef.current.contains(e.target as Node)) {
        setShowDropdown(false);
      }
    };
    document.addEventListener('mousedown', handleClick);
    return () => document.removeEventListener('mousedown', handleClick);
  }, [showDropdown]);

  const handleSelect = (name: string) => {
    onChange(VAR_PREFIX + name);
    setShowDropdown(false);
  };

  const handleClearRef = () => {
    onChange('');
  };

  // Build the effective options list, ensuring current value is always present
  const effectiveOptions = options ? ensureCurrentValue(options, strValue) : null;

  return (
    <div>
      <label className="block text-xs mb-1" style={{ color: 'var(--color-text-muted)' }}>
        {label}
      </label>
      <div className="relative flex gap-1">
        {isRef ? (
          // Show variable reference as a styled pill
          <div
            className="flex-1 flex items-center gap-1.5 text-sm px-2 py-1.5 rounded border"
            style={{
              backgroundColor: 'color-mix(in srgb, var(--color-primary) 10%, var(--color-surface-light))',
              borderColor: 'var(--color-primary)',
              color: 'var(--color-primary)',
            }}
          >
            <span className="text-[10px] font-medium px-1 py-0.5 rounded" style={{
              backgroundColor: 'var(--color-primary)',
              color: 'white',
            }}>
              {refItem ? (constants.some((c) => c.name === refItem.name) ? 'CONST' : 'VAR') : '?'}
            </span>
            <span className="font-medium truncate">{getVarName(strValue)}</span>
            <button
              onClick={handleClearRef}
              className="ml-auto text-xs opacity-60 hover:opacity-100 flex-shrink-0"
              title="Remove variable reference"
            >
              x
            </button>
          </div>
        ) : effectiveOptions ? (
          // Dropdown select mode
          <select
            value={strValue}
            onChange={(e) => onChange(e.target.value)}
            className="flex-1 text-sm px-2 py-1.5 rounded border min-w-0"
            style={{
              backgroundColor: 'var(--color-surface-light)',
              borderColor: 'var(--color-border)',
              color: 'var(--color-text)',
            }}
          >
            {effectiveOptions.map((opt) => (
              <option key={opt.value} value={opt.value}>{opt.label}</option>
            ))}
          </select>
        ) : (
          // Plain text input mode
          <input
            type="text"
            value={strValue}
            onChange={(e) => onChange(e.target.value)}
            placeholder={placeholder}
            className="flex-1 text-sm px-2 py-1.5 rounded border min-w-0"
            style={{
              backgroundColor: 'var(--color-surface-light)',
              borderColor: 'var(--color-border)',
              color: 'var(--color-text)',
            }}
          />
        )}
        {/* Variable picker button */}
        {availableItems.length > 0 && (
          <div className="relative" ref={dropdownRef}>
            <button
              onClick={() => setShowDropdown(!showDropdown)}
              className="px-1.5 py-1.5 rounded border text-[10px] font-medium flex-shrink-0"
              style={{
                backgroundColor: showDropdown ? 'var(--color-primary)' : 'var(--color-surface-light)',
                borderColor: showDropdown ? 'var(--color-primary)' : 'var(--color-border)',
                color: showDropdown ? 'white' : 'var(--color-text-muted)',
              }}
              title="Insert variable or constant"
            >
              {'{x}'}
            </button>
            {showDropdown && (
              <div
                className="absolute right-0 top-full mt-1 z-50 min-w-[180px] max-h-[200px] overflow-y-auto rounded-lg py-1 shadow-xl border"
                style={{
                  backgroundColor: 'var(--color-surface)',
                  borderColor: 'var(--color-border)',
                }}
              >
                {availableItems.length === 0 && (
                  <div className="px-3 py-2 text-xs" style={{ color: 'var(--color-text-muted)' }}>
                    No compatible variables
                  </div>
                )}
                {availableItems.map((item) => (
                  <button
                    key={item.id}
                    onClick={() => handleSelect(item.name)}
                    className="w-full text-left px-3 py-1.5 text-sm flex items-center gap-2"
                    style={{ color: 'var(--color-text)' }}
                    onMouseEnter={(e) => {
                      (e.currentTarget as HTMLElement).style.backgroundColor = 'var(--color-surface-light)';
                    }}
                    onMouseLeave={(e) => {
                      (e.currentTarget as HTMLElement).style.backgroundColor = 'transparent';
                    }}
                  >
                    <span className="text-[9px] font-medium px-1 py-0.5 rounded flex-shrink-0" style={{
                      backgroundColor: item.kind === 'constant' ? 'var(--color-accent-green)' : 'var(--color-primary)',
                      color: 'white',
                    }}>
                      {item.kind === 'constant' ? 'C' : 'V'}
                    </span>
                    <span className="truncate">{item.name}</span>
                    <span className="ml-auto text-[10px] flex-shrink-0" style={{ color: 'var(--color-text-muted)' }}>
                      {item.type}
                    </span>
                  </button>
                ))}
              </div>
            )}
          </div>
        )}
      </div>
    </div>
  );
}

/**
 * Ensure the current value is present in the options list.
 * If not, append it so the <select> always shows the correct value.
 */
function ensureCurrentValue(options: FieldOption[], currentValue: string): FieldOption[] {
  if (options.some((o) => o.value === currentValue)) return options;
  return [...options, { value: currentValue, label: currentValue }];
}
