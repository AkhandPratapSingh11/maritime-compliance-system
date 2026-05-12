import {
  useEffect,
  useState,
} from "react";

import Navbar from "../components/Navbar";

import {
  getDrills,
} from "../services/drillService";

const Drills = () => {

  const [drills, setDrills] = useState<any[]>([]);

  useEffect(() => {

    fetchDrills();

  }, []);

  const fetchDrills = async () => {

    try {

      const data = await getDrills();

      setDrills(data);

    } catch (error) {

      console.error(error);
    }
  };

  return (

    <div>

      <Navbar />

      <div style={{ padding: "20px" }}>

        <h1>Safety Drills</h1>

        <table
          border={1}
          cellPadding={10}
        >

          <thead>

            <tr>

              <th>Drill Type</th>
              <th>Ship</th>
              <th>Scheduled Date</th>

            </tr>

          </thead>

          <tbody>

            {drills.map((drill) => (

              <tr key={drill.id}>

                <td>
                  {drill.drill_type}
                </td>

                <td>
                  {drill.ship}
                </td>

                <td>
                  {drill.scheduled_date}
                </td>

              </tr>

            ))}

          </tbody>

        </table>

      </div>

    </div>
  );
};

export default Drills;