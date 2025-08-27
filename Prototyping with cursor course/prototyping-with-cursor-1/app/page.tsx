import React from "react";
import Link from "next/link";
import styles from './styles/home.module.css';

export default function Home() {
  const prototypes = [
    {
      title: 'Getting started',
      description: 'How to create a prototype',
      path: '/prototypes/example'
    },
    {
      title: 'Confetti button',
      description: 'An interactive button that creates a colorful confetti explosion',
      path: '/prototypes/confetti-button'
    },
  ];

  return (
    <div className={styles.container}>
      <header className={styles.header}>
        <h1>Arhan's prototypes</h1>
      </header>
      <main>
        <section className={styles.grid}>
          {prototypes.map((prototype, index) => (
            <Link 
              key={index}
              href={prototype.path} 
              className={styles.card}
            >
              <h3>{prototype.title}</h3>
              <p>{prototype.description}</p>
            </Link>
          ))}
        </section>
      </main>
    </div>
  );
} 