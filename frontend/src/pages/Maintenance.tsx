import {
  useEffect,
  useState,
} from "react";

import Navbar from "../components/Navbar";

import {
  getMaintenanceTasks,
  updateMaintenanceTask,
} from "../services/maintenanceService";

const Maintenance = () => {

  const [tasks, setTasks] = useState<any[]>([]);

  useEffect(() => {

    fetchTasks();

  }, []);

  const fetchTasks = async () => {

    try {

      const data = await getMaintenanceTasks();

      setTasks(data);

    } catch (error) {

      console.error(error);
    }
  };

  const handleStatusUpdate = async (
    id: number,
    status: string
  ) => {

    try {

      await updateMaintenanceTask(
        id,
        { status }
      );

      fetchTasks();

    } catch (error) {

      console.error(error);
    }
  };

  const isOverdue = (task: any) => {

    return (
      task.status !== "COMPLETED"
      &&
      new Date(task.due_date)
      <
      new Date()
    );
  };

  return (

    <div>

      <Navbar />

      <div style={{ padding: "20px" }}>

        <h1>Maintenance Tasks</h1>

        <table
          border={1}
          cellPadding={10}
        >

          <thead>

            <tr>

              <th>Title</th>
              <th>Status</th>
              <th>Due Date</th>
              <th>Overdue</th>
              <th>Actions</th>

            </tr>

          </thead>

          <tbody>

            {tasks.map((task) => (

              <tr
                key={task.id}
                style={{
                  backgroundColor:
                    isOverdue(task)
                      ? "#ffcccc"
                      : "white",
                }}
              >

                <td>{task.title}</td>
                <td>{task.status}</td>
                <td>{task.due_date}</td>

                <td>
                  {
                    isOverdue(task)
                      ? "YES"
                      : "NO"
                  }
                </td>

                <td>

                  <button
                    onClick={() =>
                      handleStatusUpdate(
                        task.id,
                        "IN_PROGRESS"
                      )
                    }
                  >
                    Start
                  </button>

                  <button
                    onClick={() =>
                      handleStatusUpdate(
                        task.id,
                        "COMPLETED"
                      )
                    }
                  >
                    Complete
                  </button>

                </td>

              </tr>

            ))}

          </tbody>

        </table>

      </div>

    </div>
  );
};

export default Maintenance;