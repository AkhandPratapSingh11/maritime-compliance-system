import { Link, useNavigate } from "react-router-dom";

const Navbar = () => {

  const navigate = useNavigate();

  const logout = () => {

    localStorage.removeItem("access");
    localStorage.removeItem("refresh");

    navigate("/");
  };

  return (

    <div
      style={{
        display: "flex",
        justifyContent: "space-between",
        alignItems: "center",
        padding: "18px 30px",
        background: "#111827",
        color: "white",
      }}
    >

      <div
        style={{
          display: "flex",
          gap: "20px",
          alignItems: "center",
        }}
      >

        <h2>
          Maritime System
        </h2>

        <Link
          to="/dashboard"
          style={{ color: "white" }}
        >
          Dashboard
        </Link>

        <Link
          to="/maintenance"
          style={{ color: "white" }}
        >
          Maintenance
        </Link>

        <Link
          to="/drills"
          style={{ color: "white" }}
        >
          Drills
        </Link>

        <Link
          to="/ships"
          style={{ color: "white" }}
        >
          Ships
        </Link>

      </div>

      <button onClick={logout}>
        Logout
      </button>

    </div>
  );
};

export default Navbar;