function StudentCard({ student, onEdit, onDelete }) {
  return (
    <div className="student-card">
      <div className="student-card-top">
        <div className="avatar">
          {student.name.charAt(0).toUpperCase()}
        </div>

        <div>
          <h4>{student.name}</h4>
          <p>{student.course}</p>
        </div>
      </div>

      <div className="student-meta">
        <span>Age: {student.age}</span>
        <span>Course: {student.course}</span>
      </div>

      <div className="student-actions">
        <button className="edit-btn" onClick={() => onEdit(student)}>
          Edit
        </button>

        <button className="delete-btn" onClick={() => onDelete(student._id)}>
          Delete
        </button>
      </div>
    </div>
  );
}

export default StudentCard;