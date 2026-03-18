import { useEffect, useMemo, useRef, useState } from "react";
import axios from "axios";
import Header from "./components/Header";
import StatsSection from "./components/StatsSection";
import StudentForm from "./components/StudentForm";
import StudentList from "./components/StudentList";

const API = "http://127.0.0.1:5000/api/students";

function App() {
  const [students, setStudents] = useState([]);
  const [searchTerm, setSearchTerm] = useState("");
  const [formData, setFormData] = useState({
    name: "",
    age: "",
    course: "",
  });
  const [editId, setEditId] = useState(null);

  const formPanelRef = useRef(null);
  const nameInputRef = useRef(null);

  const fetchStudents = async () => {
    try {
      const res = await axios.get(API + "/");
      setStudents(Array.isArray(res.data) ? res.data : []);
    } catch (err) {
      console.error("Error fetching students:", err);
    }
  };

  useEffect(() => {
    fetchStudents();
  }, []);

  const filteredStudents = useMemo(() => {
    const keyword = searchTerm.toLowerCase().trim();

    if (!keyword) return students;

    return students.filter((student) => {
      return (
        student.name.toLowerCase().includes(keyword) ||
        student.course.toLowerCase().includes(keyword) ||
        String(student.age).includes(keyword)
      );
    });
  }, [students, searchTerm]);

  const totalCourses = new Set(students.map((student) => student.course)).size;

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prev) => ({
      ...prev,
      [name]: value,
    }));
  };

  const handleAddNewStudent = () => {
    setEditId(null);
    setFormData({
      name: "",
      age: "",
      course: "",
    });

    formPanelRef.current?.scrollIntoView({
      behavior: "smooth",
      block: "start",
    });

    setTimeout(() => {
      nameInputRef.current?.focus();
    }, 300);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (!formData.name || !formData.age || !formData.course) {
      alert("Please fill all fields");
      return;
    }

    try {
      if (editId) {
        await axios.put(`${API}/${editId}`, formData);
      } else {
        await axios.post(API + "/", formData);
      }

      setFormData({
        name: "",
        age: "",
        course: "",
      });
      setEditId(null);
      fetchStudents();
    } catch (err) {
      console.error("Error saving student:", err);
    }
  };

  const handleEdit = (student) => {
    setFormData({
      name: student.name,
      age: student.age,
      course: student.course,
    });
    setEditId(student._id);

    formPanelRef.current?.scrollIntoView({
      behavior: "smooth",
      block: "start",
    });

    setTimeout(() => {
      nameInputRef.current?.focus();
    }, 300);
  };

  const handleDelete = async (id) => {
    try {
      await axios.delete(`${API}/${id}`);
      fetchStudents();
    } catch (err) {
      console.error("Error deleting:", err);
    }
  };

  return (
    <div className="page">
      <div className="container">
        <Header
          title="Student Management Dashboard"
          subtitle="Connected with Flask backend"
          buttonText="+ Add New Student"
          onButtonClick={handleAddNewStudent}
        />

        <StatsSection
          totalStudents={students.length}
          totalCourses={totalCourses}
          searchResults={filteredStudents.length}
        />

        <section className="content-grid">
          <StudentForm
            editId={editId}
            formData={formData}
            handleChange={handleChange}
            handleSubmit={handleSubmit}
            nameInputRef={nameInputRef}
            formPanelRef={formPanelRef}
          />

          <StudentList
            filteredStudents={filteredStudents}
            searchTerm={searchTerm}
            setSearchTerm={setSearchTerm}
            handleEdit={handleEdit}
            handleDelete={handleDelete}
          />
        </section>
      </div>
    </div>
  );
}

export default App;