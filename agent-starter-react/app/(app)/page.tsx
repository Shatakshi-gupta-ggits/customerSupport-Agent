import { headers } from 'next/headers';
import { getAppConfig } from '@/lib/utils';
import { App } from '@/components/app';

export default async function Page() {
  const hdrs = await headers();
  const appConfig = await getAppConfig(hdrs);

  return <App appConfig={appConfig} />;
}
