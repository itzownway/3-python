function StatsSection({ totalStudents, totalCourses, searchResults }) {
  return (
    <section className="stats-grid">
      <div className="stat-card">
        <p>Total Students</p>
        <h2>{totalStudents}</h2>
      </div>

      <div className="stat-card">
        <p>Courses</p>
        <h2>{totalCourses}</h2>
      </div>

      <div className="stat-card">
        <p>Search Results</p>
        <h2>{searchResults}</h2>
      </div>
    </section>
  );
}

export default StatsSection;