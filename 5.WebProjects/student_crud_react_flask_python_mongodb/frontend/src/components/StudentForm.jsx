function StudentForm({
  editId,
  formData,
  handleChange,
  handleSubmit,
  nameInputRef,
  formPanelRef,
}) {
  return (
    <div className="panel form-panel" ref={formPanelRef}>
      <div className="panel-header">
        <h3>{editId ? "Edit Student" : "Add Student"}</h3>
        <p>Enter student details below.</p>
      </div>

      <form onSubmit={handleSubmit} className="student-form">
        <div className="form-group">
          <label>Name</label>
          <input
            ref={nameInputRef}
            type="text"
            name="name"
            placeholder="Enter student name"
            value={formData.name}
            onChange={handleChange}
          />
        </div>

        <div className="form-group">
          <label>Age</label>
          <input
            type="number"
            name="age"
            placeholder="Enter age"
            value={formData.age}
            onChange={handleChange}
          />
        </div>

        <div className="form-group">
          <label>Course</label>
          <input
            type="text"
            name="course"
            placeholder="Enter course name"
            value={formData.course}
            onChange={handleChange}
          />
        </div>

        <div className="form-actions">
          <button type="submit" className="primary-btn full-btn">
            {editId ? "Update Student" : "Save Student"}
          </button>
        </div>
      </form>
    </div>
  );
}

export default StudentForm;