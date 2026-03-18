import StudentCard from "./StudentCard";

function StudentList({
  filteredStudents,
  searchTerm,
  setSearchTerm,
  handleEdit,
  handleDelete,
}) {
  return (
    <div className="panel list-panel">
      <div className="panel-header list-header">
        <div>
          <h3>Student Directory</h3>
          <p>View, search, edit, and delete students.</p>
        </div>

        <input
          type="text"
          className="search-input"
          placeholder="Search by name, course, age..."
          value={searchTerm}
          onChange={(e) => setSearchTerm(e.target.value)}
        />
      </div>

      <div className="student-list">
        {filteredStudents.length > 0 ? (
          filteredStudents.map((student) => (
            <StudentCard
              key={student._id}
              student={student}
              onEdit={handleEdit}
              onDelete={handleDelete}
            />
          ))
        ) : (
          <div className="empty-state">
            <h4>No students found</h4>
            <p>Try a different search keyword.</p>
          </div>
        )}
      </div>
    </div>
  );
}

export default StudentList;