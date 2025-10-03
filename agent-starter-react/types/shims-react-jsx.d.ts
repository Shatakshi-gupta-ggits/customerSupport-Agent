// Minimal shims to satisfy JSX typing in environments without @types/react installed
// This avoids false-positive lints about missing JSX.IntrinsicElements during development.

declare namespace JSX {
  interface IntrinsicElements {
    [elemName: string]: any;
  }
}

declare module 'react' {
  const React: any;
  export default React;
}



