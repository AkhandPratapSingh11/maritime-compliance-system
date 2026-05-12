import { useEffect, useState } from "react";

import Navbar from "../components/Navbar";
import DashboardCard from "../components/DashboardCard";
import Loader from "../components/Loader";

import { getDashboardData } from "../services/dashboardService";

const Dashboard = () => {

  const [data, setData] = useState<any>(null);

  useEffect(() => {

    fetchDashboard();

  }, []);

  const fetchDashboard = async () => {

    try {

      const response = await getDashboardData();

      setData(response);

    } catch (error) {

      console.error(error);
    }
  };

  if (!data) {
    return <Loader />;
  }

  return (

    <div>

      <Navbar />

      <div style={{ padding: "20px" }}>

        <h1>Dashboard</h1>

        <div
          style={{
            display: "flex",
            gap: "20px",
            flexWrap: "wrap",
          }}
        >

          <DashboardCard
            title="Total Tasks"
            value={data.maintenance.total_tasks}
          />

          <DashboardCard
            title="Overdue Tasks"
            value={data.maintenance.overdue_tasks}
          />

          <DashboardCard
            title="Missed Drills"
            value={data.drills.missed_drills}
          />

          <DashboardCard
            title="Overall Compliance"
            value={`${data.overall_compliance}%`}
          />

        </div>

      </div>

    </div>
  );
};

export default Dashboard;