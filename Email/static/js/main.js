$(function() {

    var isValidEmail = function(emailAddress) {
        if (emailAddress == undefined || emailAddress == '') {
            return false;
        }
    }
    
    // Enables select drop down
    $('.selectpicker').selectpicker();
    
    var Message = Backbone.Model.extend({
        urlRoot: "/email",
        defaults: {
            "from":  "arinks@gmail.com",
            "subject":  "",
            "message":  "",
            "type" : "1"
          },

          sync: function( method, model, options ) {
            var oldBackboneSync = Backbone.sync;
            if ( method === 'create' && options.data ) {
                options.data = JSON.stringify(options.data);
                options.contentType = 'application/json';
            } // else, business as usual.
            return oldBackboneSync.apply(this, [method, model, options]);
        }
    });

    var AppView = Backbone.View.extend({
        events: {
            "click .sendEmail": "sendEmail",
        },

        el: $("#main"),

        initialize: function(model) {
            var self = this;
            
            _.bindAll(this, 'sendEmail', 'render');

			$('#email-form').submit(_.debounce(function() {
				self.sendEmail();
			}, 500, true));
            
            $('#email-form').bootstrapValidator({
                message: 'This value is not valid',
                
                feedbackIcons: {
                    valid: 'glyphicon glyphicon-ok',
                    invalid: 'glyphicon glyphicon-remove',
                    validating: 'glyphicon glyphicon-refresh'
                },

                live: 'enabled',
				
				submitButtons: '[type="submit"]',
                
                fields: {
                    "from-email": {
                        validators: {
                            notEmpty: {
                                message: 'The email is required and cannot be empty'
                            },
                            emailAddress: {
                                message: 'The input is not a valid emptyail address'
                            }
                        }
                    },
                    "to-email": {
                        validators: {
                            notEmpty: {
                                message: 'The email is required and cannot be empty'
                            },
                            emailAddress: {
                                message: 'The input is not a valid email address'
                            }
                        }
                    },
					"cc-email": {
                        validators: {
                            emailAddress: {
                                message: 'The input is not a valid email address'
                            }
                        }
                    },
					"bcc-email": {
                        validators: {
                            emailAddress: {
                                message: 'The input is not a valid email address'
                            }
                        }
                    },
                    "subject" : "",
                    "message" : ""
                }
            });
        },

        sendEmail: function(model) {
            var self = this;
            var message = new Message();
            var form = $('#email-form');

            form.data('bootstrapValidator').validate();
            if(!form.data('bootstrapValidator').isValid()){
                return false;
            }

            message.set({
                from: $('#from-input').val(),
                to: $('#to-input').val(),
                cc: $('#cc-input').val(),
                bcc: $('#bcc-input').val(),
                subject: $('#subject-input').val(),
                message: $('#message-input').val()
            })

            message.save(null, {
                success: function(model, status){
                    $('#results-modal').on('hide.bs.modal', function() {
                        form.data('bootstrapValidator').resetForm(true);
                    })
                    
                    $('#results-modal .modal-body').html(status.text);
                    $('#results-modal').modal('show');
                },
                error: function(model, response){
                    var error = JSON.parse(response.responseText);
                    
                    $('#results-modal .modal-body').html(error['text']);
                    $('#results-modal').modal('show');
                }
            });
        },

        render: function(model) {
            this.delegateEvents();
        }

    });

    var AppRouter = Backbone.Router.extend({
        routes: {
            "send": "send"
        },

        send: function() {


        },

        initialize: function(options) {

        },

    });

    var router = new AppRouter;
    Backbone.history.start();
    new AppView;

});
