import { Link } from "react-router-dom";
import styles from "./Navbar.module.css";

export default function Navbar() {
  return (
    <nav className={styles.Navbar}>
      <Link to="/">Home</Link>
      <Link to="/translate">Translate</Link>
      <Link to="/about">About</Link>
    </nav>
  );
}
