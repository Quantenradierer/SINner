import React from "react";
import { Blockquote, Button, Card, FrameLines, FramePentagon, List, Table, Text } from "@arwes/core";
import image_path from "../../image_path";
import EditableText from "../editableText";
import AttributeList from "../attribute_list";
import active_image from "../../active_image";
import { Link } from "react-router-dom";
import { useEntity } from "../entityProvider";

const TabDefault = (props) => {
  const { entity, _} = useEntity();
  let state_label = '';
  let activeImage = active_image(entity.image_objects) || {};
  const relevantAttributes = ['type', 'appearance', 'special_features', 'remarks', 'security_systems', 'events', 'rumors_and_stories'];

  return (
    <div>
      {state_label}
      <Card
        hover
        image={{
          src: image_path('locations', activeImage.name),
          alt: entity.image_generator_description,
        }}
        title={
          <div style={{width: '100%'}}>
            <EditableText
              style={{ width: '100%' }}
              attributeName="name"
            />
          </div>
        }
      >
        <div>
          <AttributeList
            listItemWidth={130}
            attributes={relevantAttributes}
          />
        </div>
      </Card>
    </div>
  );
};

export default TabDefault;