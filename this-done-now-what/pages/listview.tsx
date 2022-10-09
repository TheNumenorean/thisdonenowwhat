import Link from 'next/link';

export default function ListView() {
  return (
    <>
      <h1>TODO LIST</h1>
      <h2>
        <Link href="/">Back to home</Link>
      </h2>
    </>
  );
}