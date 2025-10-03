import dynamic from 'next/dynamic';
import { headers } from 'next/headers';
import { getAppConfig } from '@/lib/utils';

const App = dynamic(() => import('@/components/app').then((m) => m.App), {
  ssr: false,
  loading: () => (
    <div className="mx-auto flex min-h-svh max-w-2xl items-center justify-center px-4">
      <div className="h-10 w-10 animate-spin rounded-full border-2 border-slate-600 border-t-transparent" />
    </div>
  ),
});

export default async function Page() {
  const hdrs = await headers();
  const appConfig = await getAppConfig(hdrs);

  return <App appConfig={appConfig} />;
}
