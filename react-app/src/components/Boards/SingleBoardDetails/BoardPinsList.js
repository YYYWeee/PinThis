import { useState } from "react";
import { useHistory } from "react-router-dom";

function BoardPinsList({ pins }) {
  const history = useHistory();

  pins?.sort((a, b) => new Date(a.updated_at) - new Date(b.updated_at));

  // calculate the height/width ratio for all images
  const [imageRatios, setImageRatios] = useState([]);
  const handleImageLoad = (e, index) => {
    const { naturalHeight, naturalWidth } = e.target;
    const ratio = naturalHeight / naturalWidth;
    setImageRatios((prevRatios) => {
      const updatedRatios = [...prevRatios];
      updatedRatios[index] = ratio;
      return updatedRatios;
    });
  };

  // and attach the right height class to the img
  const defaultRatios_dict = {
    s1: 0.75,
    s2: 1,
    s3: 1.25,
    s4: 1.5,
    s5: 1.78,
    s6: 1.83,
    s7: 2,
    s8: 2.3,
  };

  const defaultRatios = [0.75, 1, 1.25, 1.5, 1.78, 1.83, 2, 2.3];

  const closestRatios = [];
  for (let goal of imageRatios) {
    const closest = defaultRatios.reduce(function (prev, curr) {
      return Math.abs(curr - goal) < Math.abs(prev - goal) ? curr : prev;
    });
    closestRatios.push(closest);
  }

  const keysList = closestRatios.map((ratio) => {
    const matchingKeys = Object.keys(defaultRatios_dict).find(
      (key) => defaultRatios_dict[key] === ratio
    );
    return matchingKeys;
  });
  // console.log("imageRatios", imageRatios);
  // console.log("closestRatios", closestRatios);
  // console.log("keysList", keysList);

  return (
    <div className="pin-container1">
      {pins?.map((pin, index) => (
        // <PinsListCard key={pin.id} pin={pin} />
        <div
          key={index}
          onClick={() => history.push(`/pins/${pin.id}`)}
          className={`card-container ${keysList[index]}`}
        >
          <img
            src={pin.image_url ? pin.image_url : "no preview img"}
            alt="No pin preview"
            onLoad={(e) => handleImageLoad(e, index)}
            className="pin-card-img one"
          ></img>
          {/* {imageRatios[index] && <p>h/w Ratio: {imageRatios[index]}</p>} */}
        </div>
      ))}
      {/* <div className="pin-container">
        <MasonaryCard size="small" />
        <MasonaryCard size="medium" />
        <MasonaryCard size="large" />
        <MasonaryCard size="small" />
      </div> */}
    </div>
  );
}

export default BoardPinsList;