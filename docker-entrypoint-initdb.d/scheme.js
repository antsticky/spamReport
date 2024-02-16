var spamReport = {
   $jsonSchema: {
      bsonType: "object",
      required: ["id", "source", "sourceIdentityId", "reference", "state", "payload", "created"],
      properties: {
         id: {
            bsonType: "string"
         },
         source: {
            bsonType: "string"
         },
         sourceIdentityId: {
            bsonType: "string"
         },
         reference: {
            bsonType: "object",
            required: ["referenceId", "referenceType"],
            properties: {
               referenceId: {
                  bsonType: "string"
               },
               referenceType: {
                  bsonType: "string"
               }
            }
         },
         state: {
            bsonType: "string"
         },
         payload: {
            bsonType: "object",
            required: ["source", "reportType", "message", "reportId", "referenceResourceId", "referenceResourceType"],
            properties: {
               source: {
                  bsonType: "string"
               },
               reportType: {
                  bsonType: "string"
               },
               message: {
                  bsonType: ["string", "null"]
               },
               reportId: {
                  bsonType: "string"
               },
               referenceResourceId: {
                  bsonType: "string"
               },
               referenceResourceType: {
                  bsonType: "string"
               }
            }
         },
         created: {
            bsonType: "date"
         }
      }
   }
};

module.exports = {
   spamReport
};
