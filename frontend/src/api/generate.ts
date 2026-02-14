import { apiGet, apiPost } from './client';
import type { BlockCategory, IndicatorTemplate, StrategyData } from '../types';

export async function generateMql(strategy: StrategyData): Promise<{ code: string; filename: string }> {
  return apiPost('/generate', { data: strategy });
}

export async function getBlocks(): Promise<BlockCategory[]> {
  return apiGet('/templates/blocks');
}

export async function getIndicators(): Promise<IndicatorTemplate[]> {
  return apiGet('/templates/indicators');
}

export async function generateAiStrategy(prompt: string): Promise<{ strategy: StrategyData }> {
  return apiPost('/ai/generate-strategy', { prompt });
}
