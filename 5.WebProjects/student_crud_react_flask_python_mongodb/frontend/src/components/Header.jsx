function Header({ title, subtitle, buttonText, onButtonClick }) {
  return (
    <header className="hero">
      <div>
        <p className="eyebrow">React + Flask + MongoDB</p>
        <h1>{title}</h1>
        <p className="subtext">{subtitle}</p>
      </div>

      <button className="primary-btn" onClick={onButtonClick}>
        {buttonText}
      </button>
    </header>
  );
}

export default Header;