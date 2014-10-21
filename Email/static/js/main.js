$(function() {

    var Message = Backbone.Model.extend();

    var isValidEmail = function(emailAddress) {
        if (emailAddress == undefined || emailAddress == '') {
            return false;
        }
    }

    var AppView = Backbone.View.extend({
        events: {
            "click .sendEmail": "sendEmail",
        },

        el: $("#main"),

        initialize: function(model) {
            var self = this;
            
            _.bindAll(this, 'sendEmail', 'render');

			$('button.sendEmail').on('click', _.debounce(function() {
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
                    }
                }
            });
        },

        sendEmail: function(model) {
            alert('reached')
            var message = new Object();
            message.from = $('#from-input').val();
            message.to = $('#to-input').val();
            message.cc = $('#cc-input').val();
            message.bcc = $('#bcc-input').val();
            message.subject = $('#subject-input').val();
            message.message = $('#message-input').val();


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
