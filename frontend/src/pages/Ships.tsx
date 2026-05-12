import {
  useEffect,
  useState,
} from "react";

import Navbar from "../components/Navbar";

import {
  getShips,
} from "../services/shipService";

const Ships = () => {

  const [ships, setShips] = useState<any[]>([]);

  useEffect(() => {

    fetchShips();

  }, []);

  const fetchShips = async () => {

    try {

      const data = await getShips();

      setShips(data);

    } catch (error) {

      console.error(error);
    }
  };

  return (

    <div>

      <Navbar />

      <div style={{ padding: "20px" }}>

        <h1>Ships</h1>

        <table
          border={1}
          cellPadding={10}
        >

          <thead>

            <tr>

              <th>Name</th>
              <th>Code</th>

            </tr>

          </thead>

          <tbody>

            {ships.map((ship) => (

              <tr key={ship.id}>

                <td>{ship.name}</td>
                <td>{ship.code}</td>

              </tr>

            ))}

          </tbody>

        </table>

      </div>

    </div>
  );
};

export default Ships;