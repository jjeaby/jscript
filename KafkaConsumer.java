import ml.jjeaby.kafka

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.kafka.annotation.KafkaListener;
import org.springframework.kafka.support.Acknowledgment;
import org.springframework.kafka.support.KafkaHeaders;
import org.springframework.messaging.handler.annotation.Header;
import org.springframework.messaging.handler.annotation.Payload;
import org.springframework.stereotype.Service;
import java.util.Map;


@Slf4j
@Service
public class KafkaConsumer {
    @KafkaListener(topics = "jjeaby-topic", containerFactory = "kafkaListenerContainerFactory")
    public void receiveFromKafka(
            @Payload String message,
            @Header(KafkaHeaders.RECEIVED_PARTITION_ID) int partition, @Header(KafkaHeaders.RECEIVED_MESSAGE_KEY) String messageKey, Acknowledgment acknowledgment) throws Exception {
        log.info("Topic: [consumer] messageKey Message: [" + messageKey + "]");
        log.info("Topic: [consumer] Received Message: [" + message + "] from partition: [" + partition + "]");
        
        ...
        
        // Todo. Project's Working Coding 
        
        
        acknowledgment.acknowledge();
    }
}
